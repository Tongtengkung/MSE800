import sqlite3

def create_connection():                                            #function to create a connection to the SQLite database                        
    conn = sqlite3.connect("users.db")                                  
    return conn                                                         

def create_user_table():                                                 #function to create a table in the SQLite database                                                   
    conn = create_connection()                                          
    cursor = conn.cursor()                                             
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')

def create_inventory_table():                                          #function to create a course table in the SQLite database                                               
    conn = create_connection()                                          
    cursor = conn.cursor()                                              
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS course (
            course_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            unit INTEGER
        )
    ''')
    conn.commit()
    conn.close()
