import sqlite3
from sqlite3 import Connection

DATABASE_URL = "test.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE_URL)
    conn.row_factory = sqlite3.Row
    return conn


def query(query: str):
    conn = get_db_connection()
    rows = conn.execute(query).fetchall()
    conn.commit()
    conn.close()

    return rows


def create_tables():
    query("""
        CREATE TABLE IF NOT EXISTS lights (
            id INTEGER NOT NULL UNIQUE,
            is_on INTEGER NOT NULL DEFAULT 0
        );"""
    )

    query("INSERT OR IGNORE INTO lights(id ,is_on) VALUES(1,0),(2,0),(3,0),(4,0);")

def get_lights():
    rows = query('SELECT id, is_on FROM lights;')
    return {int(row[0]): bool(row[1]) for row in rows}

def update_light_state(light_id: int, is_on: bool):
    query(f"UPDATE lights SET is_on = {int(is_on)} WHERE id = {light_id}")
