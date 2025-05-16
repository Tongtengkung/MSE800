import sqlite3

def create_connection():                                                #function to create a connection to the SQLite database                        
    conn = sqlite3.connect("database.db")                                  
    return conn                                                         

def create_user_table():                                                #function to create a table in the SQLite database                                                   
    conn = create_connection()                                          
    cursor = conn.cursor()                                             
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')