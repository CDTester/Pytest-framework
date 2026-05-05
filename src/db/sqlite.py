"""Documentation for the sqlite module."""
import sqlite3

def create_users_table():
  """Creates the users table in the SQLite database."""
  conn = sqlite3.connect('users.db')
  cursor = conn.cursor()
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      age INTEGER NOT NULL
    )
  ''')
  conn.commit()
  conn.close()

def add_user(name: str, age: int):
  """Adds a new user to the users table."""
  conn = sqlite3.connect('users.db')
  cursor = conn.cursor()
  cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
  conn.commit()
  conn.close()
