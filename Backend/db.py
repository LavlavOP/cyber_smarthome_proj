import sqlite3
from sqlite3 import Connection

DATABASE_URL = "test.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE_URL)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_db_connection()
    conn.execute(
        """CREATE TABLE IF NOT EXISTS lights (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            is_on BOOLEAN NOT NULL DEFAULT FALSE
        );"""
    )
    conn.execute("INSERT INTO lights(ID,IS_ON) VALUES(1,0),(2,0),(3,0),(4,0)")
    conn.commit()
    conn.close()

def get_lights():
    conn = get_db_connection()
    lights = conn.execute('SELECT is_on FROM lights;').fetchall()
    conn.close()
    print(lights)
    return lights

def update_light_state(is_on):
    conn = get_db_connection()
    conn.execute('INSERT INTO lights (is_on) VALUES (?) ON CONFLICT(id) DO UPDATE SET is_on = ? WHERE id = 1;', (is_on, is_on))
    conn.commit()
    conn.close()
