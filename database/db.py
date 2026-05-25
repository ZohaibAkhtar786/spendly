import sqlite3
import os
from werkzeug.security import generate_password_hash

DB_NAME = "spendly.db"


def get_db():
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), DB_NAME)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TEXT DEFAULT (datetime('now'))
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            description TEXT,
            created_at TEXT DEFAULT (datetime('now')),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)
    conn.commit()
    conn.close()


def seed_db():
    conn = get_db()
    row = conn.execute("SELECT COUNT(*) FROM users").fetchone()
    if row[0] > 0:
        conn.close()
        return

    conn.execute(
        "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
        ("Demo User", "demo@spendly.com", generate_password_hash("demo123")),
    )

    from datetime import date, timedelta

    today = date.today()
    expenses = [
        ("Food", 25.50, today.strftime("%Y-%m-%d"), "Lunch at cafe"),
        ("Transport", 15.00, (today - timedelta(days=1)).strftime("%Y-%m-%d"), "Bus pass"),
        ("Bills", 120.00, (today - timedelta(days=2)).strftime("%Y-%m-%d"), "Electricity bill"),
        ("Health", 45.00, (today - timedelta(days=3)).strftime("%Y-%m-%d"), "Pharmacy"),
        ("Entertainment", 12.99, (today - timedelta(days=4)).strftime("%Y-%m-%d"), "Movie ticket"),
        ("Shopping", 89.99, (today - timedelta(days=5)).strftime("%Y-%m-%d"), "New shoes"),
        ("Other", 30.00, (today - timedelta(days=6)).strftime("%Y-%m-%d"), "Misc supplies"),
        ("Food", 18.75, (today - timedelta(days=7)).strftime("%Y-%m-%d"), "Dinner"),
    ]

    for category, amount, expense_date, description in expenses:
        conn.execute(
            "INSERT INTO expenses (user_id, amount, category, date, description) "
            "VALUES (1, ?, ?, ?, ?)",
            (amount, category, expense_date, description),
        )

    conn.commit()
    conn.close()