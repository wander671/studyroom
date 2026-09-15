import os
import psycopg

def conectar_banco():
    # Se o Render (ou o ambiente) fornecer uma URL completa do banco, use-a!
    database_url = os.environ.get("DATABASE_URL")
    
    if database_url:
        # Corrige o prefixo caso venha como postgres://
        if database_url.startswith("postgres://"):
            database_url = database_url.replace("postgres://", "postgresql://", 1)
        return psycopg.connect(database_url)
    
    else:
        # Caso contrário, cai nas configurações locais do seu computador (.env)
        return psycopg.connect(
            host=os.environ.get("DB_HOST", "localhost"),
            dbname=os.environ.get("DB_NAME", "seu_banco"),
            user=os.environ.get("DB_USER", "postgres"),
            password=os.environ.get("DB_PASSWORD", "sua_senha"),
            port=os.environ.get("DB_PORT", "5432")
        )