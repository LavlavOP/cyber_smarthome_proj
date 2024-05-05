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
    rows = conn.execute('SELECT id ,is_on FROM lights;').fetchall()
    conn.close()
    lights = {row[0]: row[1] for row in rows}
    return lights

def update_light_state(light_id, is_on):
    conn = get_db_connection()
    conn.execute('UPDATE lights SET is_on = ? WHERE id = ?', (1 if is_on else 0, light_id))
    conn.commit()
    conn.close()



# print(get_lights())
# update_light_state(1,1)
# print(get_lights())
# update_light_state(3,1)
# print(get_lights())

