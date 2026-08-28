# ==========================================
# STUDYROOM - ARQUIVO PRINCIPAL
# ==========================================

# Importa o Flask para criar nossa aplicação web
# e o render_template para carregar arquivos HTML
from flask import Flask, render_template

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
@app.route("/cadastro")
def cadastro():

    #Carrega a página cadastro.html
    return render_template("cadastro.html")


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
