import os
import psycopg
from database import conectar_banco

def inicializar_banco():
    print("Conectando ao banco de dados...")
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    print("Criando tabelas...")
    
    # Tabela de usuários
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            email VARCHAR(120) UNIQUE NOT NULL,
            senha VARCHAR(200) NOT NULL
        );
    """)
    
    # Tabela de fases do mapa
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS fases (
            id SERIAL PRIMARY KEY,
            titulo VARCHAR(150) NOT NULL,
            descricao TEXT,
            ordem INT NOT NULL
        );
    """)
    
    # Tabela de tópicos / aulas de cada fase
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS topicos (
            id SERIAL PRIMARY KEY,
            fase_id INT REFERENCES fases(id) ON DELETE CASCADE,
            titulo VARCHAR(150) NOT NULL,
            conteudo TEXT,
            codigo_exemplo TEXT,
            ordem INT NOT NULL
        );
    """)
    
    # Tabela de progresso do usuário
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS progresso_usuario (
            id SERIAL PRIMARY KEY,
            usuario_id INT REFERENCES usuarios(id) ON DELETE CASCADE,
            topico_id INT REFERENCES topicos(id) ON DELETE CASCADE,
            concluido BOOLEAN DEFAULT FALSE
        );
    """)
    
    conexao.commit()
    print("Tabelas criadas com sucesso!")
    
    # Inserindo dados de exemplo (Fases e Tópicos) para o Mapa não ficar vazio
    print("Inserindo fases e tópicos iniciais...")
    cursor.execute("SELECT COUNT(*) FROM fases;")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO fases (titulo, descricao, ordem) VALUES (%s, %s, %s) RETURNING id;", 
                       ("Fase 1: Fundamentos de Python e Lógica", "Inicie sua jornada dominando a base da programação.", 1))
        fase_1_id = cursor.fetchone()[0]
        
        cursor.execute("INSERT INTO topicos (fase_id, titulo, conteudo, codigo_exemplo, ordem) VALUES (%s, %s, %s, %s, %s);",
                       (fase_1_id, "Variáveis e Tipos de Dados", "Entenda como armazenar informações na memória.", "nome = 'Wander'\nprint(nome)", 1))
        cursor.execute("INSERT INTO topicos (fase_id, titulo, conteudo, codigo_exemplo, ordem) VALUES (%s, %s, %s, %s, %s);",
                       (fase_1_id, "Estruturas Condicionais", "Tomando decisões no código com if, elif e else.", "if idade >= 18:\n    print('Maior de idade')", 2))
        
        cursor.execute("INSERT INTO fases (titulo, descricao, ordem) VALUES (%s, %s, %s);", 
                       ("Fase 2: Banco de Dados e SQL", "Aprenda a gerenciar dados com MySQL e PostgreSQL.", 2))
        
        conexao.commit()
        print("Dados iniciais inseridos com sucesso!")
    else:
        print("O banco já possui fases cadastradas.")

    cursor.close()
    conexao.close()

if __name__ == "__main__":
    inicializar_banco()