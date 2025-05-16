import sqlite3

def create_connection():                                                #function to create a connection to the SQLite database                        
    conn = sqlite3.connect("database.db")                                  
    return conn                                                         

def create_user_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            password TEXT NOT NULL,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            telephone TEXT,
            address TEXT
        )
    ''')
    conn.commit()
    conn.close()