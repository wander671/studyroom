# ==========================================
# STUDYROOM - TESTE DE CONEXÃO
# ==========================================

# Importa a função de conexão criada
# no arquivo database.py
from database import conectar_banco

# ==========================================
# TESTE DA CONEXÃO
# ==========================================

try:
    # Tenta conectar ao PostgreSQL
    conexao = conectar_banco()

    # Se chegou aqui, a conexão funcionou
    print("=============================================")
    print("CONEXÂO REALIZADA COM SUCESSO!")
    print("StudyRoom conectado ao PostgreSQL! 📚🐘")
    print("=============================================")

    # ==========================================
    # ENCERRAMENTO DA CONEXÃO
    # ==========================================

    # Fecha a conexão após o teste
    conexao.close()

    print("Conexão encerrada com segurança. 🔒")


# ==========================================
# TRATAMENTO DE ERRO
# ==========================================
except Exception as erro:

    # Mostra o erro caso a conexão falhe
    print("===========================================")
    print("ERRO AO CONECTAR COM O BANCO! ❌")
    print("===========================================")

    print(erro)
