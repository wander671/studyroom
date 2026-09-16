import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

def conectar_banco():
    database_url = os.getenv("DATABASE_URL")
    
    if database_url:
        if database_url.startswith("postgres://"):
            database_url = database_url.replace("postgres://", "postgresql://", 1)
        return psycopg.connect(database_url)
    
    # Se não houver DATABASE_URL, monta a conexão localmente
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432")
    dbname = os.getenv("DB_NAME", "studyroom")
    user = os.getenv("DB_USER", "postgres")
    password = os.getenv("DB_PASSWORD", "")
    
    # Se a senha estiver vazia, conecta sem o parâmetro de senha
    if password:
        return psycopg.connect(host=host, port=port, dbname=dbname, user=user, password=password)
    else:
        return psycopg.connect(host=host, port=port, dbname=dbname, user=user)