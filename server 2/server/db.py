import os
import sqlite3
from contextlib import contextmanager

from consts import ROOT_DIR

DATABASE_PATH = os.path.join(ROOT_DIR, "test.db")


@contextmanager
def get_db():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    yield conn
    conn.commit()
    conn.close()


def query(query_str: str):
    with get_db() as conn:
        rows = conn.execute(query_str).fetchall()

    return rows


def run_schema():
    schema_path = os.path.join(ROOT_DIR, "schema.sql")
    with open(schema_path) as f:
        schema = f.read()

    with get_db() as conn:
        conn.executescript(schema)


def get_lights():
    rows = query('SELECT id, is_on FROM lights;')
    return {int(row[0]): bool(row[1]) for row in rows}


def update_light_state(light_id: int, is_on: bool):
    query(f"UPDATE lights SET is_on = {int(is_on)} WHERE id = {light_id}")


def authenticate_user(username: str, hashed_password: str) -> bool:
    rows = query(f"SELECT username FROM users WHERE username = '{username}' AND hashed_password = '{hashed_password}'")
    return len(rows) > 0
