import sqlite3

def get_db_connection():
    conn = sqlite3.connect('snake_ladder_game.db')
    conn.row_factory = sqlite3.Row
    return conn

# Additional database functions can be added here.