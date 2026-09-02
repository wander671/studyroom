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
from flask import Flask, render_template, request, flash
from database import conectar_banco
from werkzeug.security import generate_password_hash

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
# ROTA PRINCIPAL
# ==========================================

# Define a rota "/" (página inicial)
@app.route("/")
def home():

    # Renderiza o arquivo index.html localizado
    # dentro da pasta templates
    return render_template("index.html")

# ==========================================
# ROTA DE LOGIN
# ==========================================

# Define a rota "/login"
@app.route("/login")
def login():

    # Carrega a página login.html
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
            return render_template("Cadastro.html")

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

        print("Usuário cadastrado com sucesso no banco!")

    # ==========================================
    # Esse return é o "padrão":
    # roda quando o método é GET (visita normal),
    # ou quando o POST terminou o cadastro com sucesso
    # ==========================================
    return render_template("Cadastro.html")

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
        return "StudyRoom conectado ao PostgreSQL! 🐘"
    except Exception as erro:
        # Captura qualquer erro na conexão com o banco
        print(f"Erro ao conectar ao PostgreSQL: {erro}")
        return "Erro ao conectar ao PostgreSQL.", 500


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
