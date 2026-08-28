# ==========================================
# STUDYROOM - CONEXÃO COM POSTGRESQL
# ==========================================

# Importa o psycopg
# Biblioteca responsável pela comunicação
# entre o Python e o PostgreSQL
import psycopg
# Importa o load_dotenv
# Responsável por carregar as variáveis
# armazenadas no arquivo .env
from dotenv import load_dotenv
# Importa o módulo os
# Utilizado para acessar variáveis de ambiente
import os

# ==========================================
# CARREGAMENTO DAS VARIÁVEIS DE AMBIENTE
# ==========================================

# Carrega as informações armazenadas
# no arquivo .env
load_dotenv()

# ==========================================
# CONFIGURAÇÕES DO BANCO DE DADOS
# ==========================================

# Endereço onde o PostgreSQL está rodando
DB_HOST = "localhost"
# Porta padrão utilizada pelo PostgreSQL
DB_PORT = 5432
# Nome do banco de dados do StudyRoom
DB_NAME = "studyroom_db"
# Usuário utilizado para acessar o PostgreSQL
DB_USER = "postgres"
# Senha do usuário postgres
#
# A senha é recuperada do arquivo .env
# para não ficar exposta diretamente no código
DB_PASSWORD = os.getenv("DB_PASSWORD")

# ==========================================
# FUNÇÃO DE CONEXÃO
# ==========================================
def conectar_banco():
    """
    Cria uma conexão com o banco de dados
    PostgreSQL do StudyRoom.
    """
    # Estabelece a conexão com o PostgreSQL
    conexao = psycopg.connect(

        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

    # Retorna a conexão para quem chamar
    # esta função
    return conexao
