# ==========================================
# STUDYROOM - ARQUIVO PRINCIPAL
# ==========================================

# Importa o Flask para criar nossa aplicação web,
# o render_template para carregar arquivos HTML
# e a função conectar_banco para conectar
# nossa aplicação ao PostgreSQL.
# O "request" é o objeto que guarda os dados
# enviados pelo formulário (POST) ou pela URL (GET)
# Precisamos do "os" para ler variáveis
# de ambiente do arquivo .env
# Adicionamos "flash" na importação do Flask
# Ele permite guardar mensagens temporárias
# para exibir ao usuário (ex: erros, avisos)
# generate_password_hash: transforma a senha
# em um hash seguro e irreversível antes de salvar
import os
from flask import Flask, render_template, request, flash, session, redirect, url_for
from database import conectar_banco
from werkzeug.security import generate_password_hash, check_password_hash

# ==========================================
# CRIAÇÃO DA APLICAÇÃO
# ==========================================

# Cria uma instância da aplicação Flask
app = Flask(__name__)

# A SECRET_KEY é usada pelo Flask para proteger
# dados da sessão (como as mensagens do flash())
# contra adulteração. Ela é carregada do .env
# para não ficar exposta no código.
app.secret_key = os.environ.get("SECRET_KEY")

# ==========================================
# IMPORTAÇÃO NECESSÁRIA
# ==========================================

# "wraps" preserva o nome/metadados da função
# original quando ela é "envolvida" pelo decorator
# (sem isso, o Flask pode se confudir entre rotas)
from functools import wraps

# ==========================================
# DECORATOR: LOGIN OBRIGATÓRIO
# ==========================================
def login_obrigatorio(funcao):
    """
    Decorator que verifica se o usuário está logado
    antes de permitir o acesso à rota.

    Se não estiver logado, redireciona para /login.
    Se estiver logado, executa a rota normalmente

    """
    @wraps(funcao)
    def funcao_protegida(*args, **kwargs):

        #Verifica de existe um usuario_id na sessão
        if "usuario_id" not in session:

            flash("você precisa estar logado para acessar essa página." "erro")
            return redirect(url_for("login"))

        # Se está logado, executa a rota normalmente
        return funcao(*args, **kwargs)

    return funcao_protegida

# ==========================================
# ROTA PRINCIPAL
# ==========================================

# Define a rota "/" (página inicial)
@app.route("/")
def home():

    # Renderiza o arquivo index.html localizado
    # dentro da pasta templates
    return render_template("index.html")

# ==========================================
# ROTA DE LOGOUT
# ==========================================
@app.route("/logout")
def logout():
    # Limpa todos os dados da sessão do usuário
    session.clear()
    # Redireciona para a página inial pública (home)
    return redirect(url_for("home"))
# ==========================================
# ROTA DE LOGIN
# ==========================================

# Define a rota "/login"
@app.route("/login", methods=["GET", "POST"])
def login():

    # Verifica qual foi o método usado na requisição
    if request.method == "POST":
        # Aqui você pode adicionar a lógica de autenticação
        # usando os dados enviados pelo formulário.
        # Por exemplo, você pode buscar o usuário no banco
        # e verificar se a senha está correta.
        email = request.form["email"]
        senha = request.form["senha"]
       

# ==========================================
# BUSCA O USUÁRIO NO BANCO PELO EMAIL
# ==========================================
        # Abre uma conexão com o PostgreSQL
        conexao = conectar_banco()
        # O cursor é o "objeto" que executa comandos SQL
        curso = conexao.cursor()
        # Busca um usuário que tenha esse email
        curso.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        # fetchone() pega o primeiro resultado encontrado
        # Se não encontrar ninguém, retorna None
        usuario = curso.fetchone()
        # Fecha o cursor e a conexão, liberando recursos
        curso.close()
        conexao.close()

        
# ==========================================
# VERIFICA SE O USUÁRIO EXISTE
# ==========================================
        if usuario is None:
            flash("Usuário não encontrado. Por favor, verifique o email.", "erro")
            return render_template("login.html")
# ==========================================
# VERIFICA SE A SENHA ESTÁ CORRETA
# ==========================================
        senha_hash = usuario[3]  # Supondo que a senha esteja na quarta coluna

        if not check_password_hash(senha_hash,senha):
            flash("Senha incorreta. Por favor, tente novamente.", "erro")
            return render_template("login.html")
# ==========================================
# LOGIN VÁLIDO!
# ==========================================
        # Guarda o id do usuário na sessão.
        # Isso "lembra" que ele está logado enquanto
        # navega pelo site, até fazer logout ou fechar
        # o navegador (dependendo da configuração).
        session["usuario_id"] = usuario[0]

        flash(f"Bem-vindo(a), {usuario[1]}!", "sucesso")   

        # Redireciona para a página do mapa,
        # já que o login foi bem-sucedido
        return redirect(url_for("mapa"))
    return render_template("login.html")

# ==========================================
# ROTA DE RECUPERAÇÃO DE SENHA
# ==========================================
@app.route("/esqueci-senha", methods=["GET", "POST"])
def esqueci_senha():
    if request.method == "POST":
        email = request.form["email"]
        nova_senha = request.form["nova_senha"]

        conexao = conectar_banco()
        cursor = conexao.cursor()

        # Verifica se o e-mail existe
        cursor.execute("SELECT id FROM usuarios WHERE email = %s", (email,))
        usuario = cursor.fetchone()

        if usuario is None:
            cursor.close()
            conexao.close()
            flash("E-mail não encontrado no sitema.", "erro")
            return render_template("esqueci_senha.html")

        # Atualiza a senha com o novo hash
        novo_hash = generate_password_hash(nova_senha)
        cursor.execute("UPDATE usuarios SET senha = %s WHERE email = %s", (novo_hash, email))
        conexao.commit()

        cursor.close()
        conexao.close()

        flash("senha alterada com sucesso! Faça login com a nova senha." "secesso")
        return redirect(url_for("login"))

    return render_template("esqueci_senha.html")

# ==========================================
# ROTA DE CADASTRO
# ==========================================

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    # Verifica qual foi o método usado na requisição
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]
        confirmar_senha = request.form["confirmar_senha"]
        
        # ==========================================
        # VALIDAÇÃO: as senhas digitadas são iguais?
        # ==========================================
        if senha != confirmar_senha:
            flash("As senhas não conferem. Por favor, tente novamente.", "erro")
            return render_template("cadastro.html")

        # GERA O HASH DA SENHA
        senha_hash = generate_password_hash(senha)
        
        # ==========================================
        # SALVA O USUÁRIO NO BANCO DE DADOS
        # ==========================================
        try:
            conexao = conectar_banco()
            cursor = conexao.cursor()
            
            cursor.execute(
                "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)",
                (nome, email, senha_hash)
            )
            conexao.commit()
            
            cursor.close()
            conexao.close()

            flash("Usuário cadastrado com sucesso! Faça login para continuar.", "sucesso")
            return redirect(url_for("login"))
            
        except Exception as e:
            print(f"Erro no cadastro: {e}")
            flash("Este e-mail já está cadastrado ou ocorreu um erro no sistema.", "erro")
            return render_template("cadastro.html")

    # Retorna a página de cadastro padrão quando o método for GET
    return render_template("cadastro.html")

# ==========================================
# ROTA DE TESTE DO BANCO DE DADOS
# ==========================================
@app.route("/teste-banco")
def teste_banco():
    try:
        # Tenta estabelecer uma conexão com o PostgreSQL
        conexao = conectar_banco()
        # Fecha a conexão após o teste
        conexao.close()
        # Retorna uma mensagem informando que a conexão funcionou
        flash("Conexão com o PostgreSQL estabelecida com sucesso!", "sucesso")
        return "StudyRoom conectado ao PostgreSQL! 🐘"
    except Exception as erro:
        # Captura qualquer erro na conexão com o banco
        flash("Erro ao conectar ao PostgreSQL.", "erro")
        return "Erro ao conectar ao PostgreSQL.", 500

# ==========================================
# ROTA DO MAPA DE CARREIRA
# ==========================================
@app.route("/mapa")
@login_obrigatorio
def mapa():

    conexao = conectar_banco()
    cursor = conexao.cursor()

    # Busca todas as fases ordenadas pela coluna 'ordem'
    cursor.execute("SELECT id, titulo, descricao FROM fases ORDER BY ordem ASC;")
    fases_db = cursor.fetchall()

    # Lista para estruturar as fases junto com os tópicos correspondentes
    fases_com_topicos = []

    for fase in fases_db:
        fase_id = fase[0]
        fase_titulo = fase[1]
        fase_descricao = fase[2]

        # Para cada fase, busca os tópicos cadastrados no banco
        cursor.execute("""
            SELECT id, titulo, conteudo, codigo_exemplo
            FROM topicos
            WHERE fase_id = %s
            ORDER BY ordem ASC;
        """, (fase_id,))
        topicos_db = cursor.fetchall()

        # Guardamos a fase com seus respectivos tópicos
        fases_com_topicos.append({
            "id": fase_id,
            "titulo": fase_titulo,
            "descricao": fase_descricao,
            "topicos": topicos_db
        })

    cursor.close()
    conexao.close()

    # Renderiza o template do mapa
    return render_template("mapa.html", fases=fases_com_topicos)

# ==========================================
# ROTA TEMPORÁRIA DE DIAGNÓSTICO (FASES)
# ==========================================
@app.route("/debug-fases")
def debug_fases():
    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, ordem, titulo FROM fases ORDER BY ordem ASC;")
        fases = cursor.fetchall()
        cursor.close()
        conexao.close()

        # Retorna a lista de fases e seus IDs na tela
        return {"fases_cadastradas": fases}
    except Exception as e:
        # Se der erro, mostra o erro exato na tela para a gente resolver
        return {"erro_no_banco": str(e)}



# ==========================================
# EXECUÇÃO DA APLICAÇÃO
# ==========================================

# Este bloco executa somente quando
# rodamos diretamente o arquivo run.py
if __name__ == "__main__":

    # Inicia o servidor Flask em modo debug
    # O debug facilita o desenvolvimento porque
    # mostra erros e reinicia automaticamente
    app.run(debug=True)
