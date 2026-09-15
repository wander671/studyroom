import os
import psycopg

def conectar_banco():
    # Cole a sua Internal Database URL do Render aqui dentro das aspas:
    database_url = "postgresql://studyroom_db_6gps_user:pNbD1CetaLqQySM4suCaAjZsU9Y8h9Jb@dpg-daji8t1594qs73caf4u0-a/studyroom_db_6gps"
    
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)
        
    return psycopg.connect(database_url)