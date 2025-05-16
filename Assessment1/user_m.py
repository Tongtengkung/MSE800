from database import create_connection
import sqlite3

def register_account(user_id, name, email, password, telephone, address):
    conn = create_connection()                                                              
    cursor = conn.cursor()                                                                  
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (user_id, name, email, password, telephone, address))      
        conn.commit()                                                                       
        print(" User added successfully.")                                                  
    except sqlite3.IntegrityError:                                                          
        print(" Email must be unique.")
    conn.close()                                                                                                                                                                                                             

def sign_in(user_id, password):
    conn = create_connection()                                                              
    cursor = conn.cursor()                                                                  
    cursor.execute("SELECT * FROM users WHERE user_id = ? AND password = ?", (user_id, password)) 
    user = cursor.fetchone()                                                                
    if user:
        print("Sign in successful.")
        return True
    else:
        print("Invalid user ID or password.")
        return False

def delete_user(user_id):
    conn = create_connection()                                                              
    cursor = conn.cursor()                                                                  
    cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))                         
    conn.commit()                                                                            
    if cursor.rowcount > 0:
        print("User deleted successfully.")
    else:
        print("No user found with the specified ID.")
    conn.close()