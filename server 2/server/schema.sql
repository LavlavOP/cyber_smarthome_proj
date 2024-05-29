CREATE TABLE IF NOT EXISTS lights (
    id    INTEGER NOT NULL UNIQUE,
    is_on INTEGER NOT NULL DEFAULT 0
);

INSERT OR IGNORE INTO lights(id ,is_on) VALUES(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0);

CREATE TABLE IF NOT EXISTS users (
    username TEXT NOT NULL UNIQUE,
    hashed_password TEXT NOT NULL
);
