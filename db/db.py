import sqlite3
from datetime import date

DB_NAME = "entries.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    with open("db/schema.sql", "r") as f:
        cursor.executescript(f.read())
    conn.commit()
    conn.close()

def add_entry(journal, intention, dream, priorities, reflection, strategy):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO entries (date, journal, intention, dream, priorities, reflection, strategy)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (str(date.today()), journal, intention, dream, priorities, reflection, strategy))
    conn.commit()
    conn.close()

def get_entries():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, date, journal, intention, dream, priorities, reflection, strategy FROM entries")
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_entry_by_date(entry_date):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM entries WHERE date = ?", (entry_date,))
    row = cursor.fetchone()
    conn.close()
    return row
