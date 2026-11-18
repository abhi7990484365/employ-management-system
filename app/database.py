import os
import sqlite3
from pathlib import Path

DB_PATH = os.getenv("EMPLOYEE_DB_PATH", str(Path(__file__).resolve().parent.parent / "employees.db"))

def connect():
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    return db

def initialize():
    with connect() as db:
        db.execute("""CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            department TEXT NOT NULL
        )""")
