"""
TechSolve S.A. -- Soporte Técnico Nivel 1
Script de inicialización de la base de datos
"""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'techsolve.db')
SCHEMA  = os.path.join(os.path.dirname(__file__), 'schema.sql')
SEED    = os.path.join(os.path.dirname(__file__), 'seed_data.sql')


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    with open(SCHEMA, 'r', encoding='utf-8') as f:
        cursor.executescript(f.read())

    with open(SEED, 'r', encoding='utf-8') as f:
        cursor.executescript(f.read())

    conn.commit()
    conn.close()
    print(f"Base de datos inicializada en: {os.path.abspath(DB_PATH)}")


if __name__ == '__main__':
    init_db()
