# ==========================================
# STUDYROOM - ARQUIVO PRINCIPAL
# ==========================================

# Importa o Flask para criar nossa aplicação web
from flask import Flask

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
    # Retorna uma mensagem simples para testar
    # se o servidor Flask está funcionando
    return"StudyRoom funcionando!📚"

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
