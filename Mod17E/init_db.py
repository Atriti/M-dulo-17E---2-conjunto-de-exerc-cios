import sqlite3
import os

print("Base de dados criada em:", os.path.abspath("database.db"))
# Criar ligação
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

print("Ligação criada.")

# ============================
# CRIAR A TABELA USERS
# ============================

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    perfil TEXT NOT NULL DEFAULT "user"
)
""")

print("Tabela users criada.")

cursor.execute ("""INSERT INTO users (username, email, password, perfil) VALUES ('ana', 'ana@example.com', "123", "admin")""")
cursor.execute ("""INSERT INTO users (username, email, password, perfil) VALUES ('joao', 'joao@example.com', "abc", "user")""")

print("Utilizadores inseridos.")


# ============================
# CRIAR A TABELA RECURSOS
# ============================

cursor.execute("""
CREATE TABLE IF NOT EXISTS recursos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT UNIQUE,
    descricao TEXT
)
""")

print("Tabela recursos criada.")

cursor.execute("""INSERT INTO recursos (nome, descricao) VALUES ("Sala 1", "Sala de reuniões")""")
cursor.execute("""INSERT INTO recursos (nome, descricao) VALUES ("Projetor", "Projetor HD")""")
cursor.execute("""INSERT INTO recursos (nome, descricao) VALUES ("Laboratório", "Laboratório de informática")""")

print("Recursos inseridos.")


# ==================================
# CRIAR A TABELA RESERVAS (AULA 26)
# PARA ATUALIZAR A TABELA RECURSOS
#ELIMINEI A ANTIGA
# ==================================


cursor.execute("""
CREATE TABLE reservas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    recurso_id INTEGER,
    data TEXT,
    hora TEXT,
    observacoes TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (recurso_id) REFERENCES recursos(id)
)
""")

print("Tabela reservas criada.")


# ============================
# FINALIZAR
# ============================

conn.commit()
conn.close()

print("Base de dados criada com sucesso!")
