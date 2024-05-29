import sqlite3

def initialize_db(user_id, username, first_name, last_name):
    conn = sqlite3. connect('bot_database.dp')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT
            user_id INTEGER NOT NULL,
            username TEXT,
            first_name TEXT,
            last_name TEXT
        )
    ''')
    conn.commit()
    conn.close()

def initialize_db(user_id, username, first_name, last_name):
    conn = sqlite3. connect('bot_database.dp')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO user (user_id, username, first_name, last_name)
        VALUS (?, ?, ?)
    ''',(user_id, username, first_name, last_name)
    conn.commit()
    conn.close()

def get_user(user_id):
    conn = sqlite3.connect('bot_database.dp')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM users WHERE user_id = ?
    ''', (user_id,))
    conn.commit()
    conn.cursor()
    return user_id

def add_user(user_id, username, firs_name, last_name):
    conn = sqlite3.connect('bot_database.dp')
    cursor = conn.cursor
