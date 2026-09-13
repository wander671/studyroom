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

# Remove o usuario_id da sessão
# pop() remove o item e retorna o valor removido
# (não vamos usar o valor aqui, só queremos remover)
    session.pop("usuario_id", None)

    # Avisa o usuário que ele saiu com sucesso
    flash("Você saiu da sua conta.", "sucesso")

    # Redireciona o usuário para a página de login
    return redirect(url_for("login"))

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

        # Redireciona para a página de trilhas,
        # já que o login foi bem-sucedido
        return redirect(url_for("trilhas"))
    return render_template("login.html")

# ==========================================
# ROTA DE CADASTRO
# ==========================================

# Define a rota "/cadastro"
@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    # Verifica qual foi o método usado na requisição
    if request.method == "POST":
        # request.form["nome_do_campo"] busca o valor
        # digitado pelo usuário, usando o "name" do input
        # como se fosse uma chave de dicionário
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]
        confirmar_senha = request.form["confirmar_senha"]
        # ==========================================
        # VALIDAÇÃO: as senhas digitadas são iguais?
        # ==========================================
        if senha != confirmar_senha:
            # flash() guarda uma mensagem temporária
            # que pode ser exibida no HTML depois
            flash("As senhas não conferem. Por favor, tente novamente.", "erro")
        
            # Aqui sim: se deu erro, mostramos a página
            # de cadastro de novo, sem salvar nada
            return render_template("cadastro.html")

# ==========================================
# GERA O HASH DA SENHA
# ==========================================

        # Nunca salvamos a senha em texto puro no banco.
        # generate_password_hash transforma a senha
        # original em um código embaralhado e seguro.
        senha_hash = generate_password_hash(senha)
        

        
# ==========================================
# SALVA O USUÁRIO NO BANCO DE DADOS
# ==========================================

        # Abre uma conexão com o PostgreSQL
        conexao = conectar_banco()

        # O cursor é o "objeto" que executa comandos SQL
        cursor = conexao.cursor()

        # Executa o INSERT, usando %s como placeholders
        # para evitar SQL Injection (nunca montar a query
        # colando as variáveis direto na string!)
        cursor.execute(
            "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)",
            (nome, email, senha_hash)
        )

        # commit() confirma a alteração no banco
        # (sem isso, o INSERT não é salvo de verdade)
        conexao.commit()

        # Fecha o cursor e a conexão, liberando recursos
        cursor.close()
        conexao.close()

        flash("Usuário cadastrado com sucesso!", "sucesso")

    # ==========================================
    # Esse return é o "padrão":
    # roda quando o método é GET (visita normal),
    # ou quando o POST terminou o cadastro com sucesso
    # ==========================================
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
# ROTA DE DETALHES DA TRILHA
# ==========================================
@app.route("/trilha/<int:trilha_id>")
@login_obrigatorio
def trilha(trilha_id):

    conexao = conectar_banco()
    cursor = conexao.cursor()

    # Busca os dados da trilha
    cursor.execute(
        "SELECT id, titulo, descricao, nivel FROM trilhas WHERE id = %s",
        (trilha_id,)
    )
    dados_trilha = cursor.fetchone()

    # Busca os módulos de trilha, em ordem
    cursor.execute(
        "SELECT id, titulo, ordem FROM modulos WHERE trilha_id = %s ORDER BY ordem",
        (trilha_id,)
    )
    modulos = cursor.fetchall()

# ==========================================
# BUSCA AS AULAS DE CADA MÓDULO
# ==========================================
    
    # Vamos guadar aqui uma lista de dicionários,
    # onde cada item representa um módulo JUNTO
    # com suas salas
    modulos_com_aulas = []

    # Percorre cada módulo da lista que ja buscamos
    for modulo in modulos:

        # modulo[0] é o id do módulo específico, em ordem
        modulo_id = modulo[0]

        # Busca as aulas desse módulo específico, em ordem
        cursor.execute(
            "SELECT id, titulo, arquivo_pdf, ordem FROM aulas WHERE modulo_id = %s ORDER BY ordem",
            (modulo_id,)
        )
        aulas = cursor.fetchall()

        # Monta um dicionário juntando os dados do módulo
        # com a lista de aulas dele
        modulos_com_aulas.append({
            "id": modulo[0],
            "titulo": modulo[1],
            "ordem":modulo[2],
            "aulas": aulas
        })

    cursor.close()
    conexao.close()

    print(f"Trilha encontrada: {dados_trilha}")
    print(f"Módulos com aulas: {modulos_com_aulas}")

    return render_template(
        "trilha_detalhes.html",
        trilha=dados_trilha,
        modulos=modulos_com_aulas
    )

# ==========================================
# ROTA DE LISTAGEM DE TRILHAS
# ==========================================
@app.route("/trilhas")
@login_obrigatorio
def trilhas():

    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("SELECT id, titulo, descricao, nivel FROM trilhas")
    lista_trilhas = cursor.fetchall()

    cursor.close()
    conexao.close()

    return render_template("trilhas_lista.html", trilhas=lista_trilhas)


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
