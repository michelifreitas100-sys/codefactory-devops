"""
Script de inicialização do banco de dados.
Executado dentro de um container próprio (ver docker-compose.yml)
para demonstrar o uso de containers também para tarefas de banco de dados,
conforme pede o critério 5 (Utilização de containers - Docker).
"""
import os
import time

import psycopg2

DB_HOST = os.environ.get("DB_HOST", "db")
DB_NAME = os.environ.get("DB_NAME", "codefactory")
DB_USER = os.environ.get("DB_USER", "codefactory")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "codefactory")


def wait_for_db(retries=10, delay=3):
    for attempt in range(1, retries + 1):
        try:
            conn = psycopg2.connect(
                host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD
            )
            return conn
        except psycopg2.OperationalError:
            print(f"[init_db] Banco ainda não disponível (tentativa {attempt}/{retries})...")
            time.sleep(delay)
    raise RuntimeError("Não foi possível conectar ao banco de dados.")


def create_tables():
    conn = wait_for_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            done BOOLEAN DEFAULT FALSE,
            created_at TIMESTAMP DEFAULT NOW()
        );
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("[init_db] Tabela 'tasks' criada/verificada com sucesso.")


if __name__ == "__main__":
    create_tables()
