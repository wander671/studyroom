# ==========================================
# STUDYROOM - ARQUIVO PRINCIPAL
# ==========================================

# Importa o Flask para criar nossa aplicação web,
# o render_template para carregar arquivos HTML
# e a função conectar_banco para conectar
# nossa aplicação ao PostgreSQL.
# O "request" é o objeto que guarda os dados
# enviados pelo formulário (POST) ou pela URL (GET)
from flask import Flask, render_template, request
from database import conectar_banco

# ==========================================
# CRIAÇÃO DA APLICAÇÃO
# ==========================================

# Cria uma instância da aplicação Flask
app = Flask(__name__)

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
        # Por enquanto, vamos só imprimir no terminal
        # pra confirmar que está pegando certinho
        print(f"Nome: {nome}")
        print(f"Email: {email}")
        print(f"Senha: {senha}")
        print(f"Confirmar senha: {confirmar_senha}")
        pass

    #Carrega a página cadastro.html
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
