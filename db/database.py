import sqlite3
from pathlib import Path

DB_PATH = Path("data/support_tickets.db")

def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DB_PATH, check_same_thread=False)
