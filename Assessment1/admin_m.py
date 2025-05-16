from database import create_connection
import sqlite3

def admin_add_user(user_id, name, email, password, telephone, address):
    conn = create_connection()                                                              #สร้างการเชื่อมต่อกับฐานข้อมูล
    cursor = conn.cursor()                                                                  #ใช้สำหรับการสร้าง cursor object
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))      #ใช้สำหรับการเพิ่มข้อมูลลงในตาราง users
        conn.commit()                                                                       #ใช้สำหรับการบันทึกการเปลี่ยนแปลงในฐานข้อมูล
        print(" User added successfully.")                                                  #แสดงข้อความเมื่อเพิ่มข้อมูลสำเร็จ
    except sqlite3.IntegrityError:                                                          #ใช้สำหรับการจัดการข้อผิดพลาดที่เกิดจากการละเมิดความสมบูรณ์ของข้อมูล
        print(" Email must be unique.")                                                     #แสดงข้อความเมื่ออีเมลซ้ำ
    conn.close()                                                                            #ปิดการเชื่อมต่อกับฐานข้อมูล

def admin_change_user(user_id, name=None, email=None, password=None, telephone=None, address=None):
    """
    Update user information based on user_id.
    Only the fields provided (non-None) will be updated.
    """
    conn = create_connection()
    cursor = conn.cursor()
    
    fields = []
    values = []

    if name is not None:
        fields.append("name = ?")
        values.append(name)
    if email is not None:
        fields.append("email = ?")
        values.append(email)
    if password is not None:
        fields.append("password = ?")
        values.append(password)
    if telephone is not None:
        fields.append("telephone = ?")
        values.append(telephone)
    if address is not None:
        fields.append("address = ?")
        values.append(address)

    if not fields:                                                                      # No fields to update
        print("No fields to update.")
        conn.close()
        return

    sql = f"UPDATE users SET {', '.join(fields)} WHERE id = ?"                          # Prepare the SQL statement
    values.append(user_id)

    try:
        cursor.execute(sql, tuple(values))
        conn.commit()

        if cursor.rowcount > 0:
            print("User information updated successfully.")
        else:
            print("No user found with the specified ID.")
    except sqlite3.IntegrityError as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()                                          

def admin_view_user():                                                                           #function to view all users
    conn = create_connection()                                                              
    cursor = conn.cursor()                                                                  
    cursor.execute("SELECT * FROM users")                                                   #function to select all users from the database                                                      
    rows = cursor.fetchall()                                                                #function to fetch all rows from the database                       
    conn.close()                                                                           
    return rows                                                                             

def admin_search_user(name):                                                                      
    conn = create_connection()                                                              
    cursor = conn.cursor()                                                                  
    cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + name + '%',))            
    rows = cursor.fetchall()                                                               
    conn.close()                                                                               
    return rows                                                                             

def admin_delete_user(user_id):                                                                   
    conn = create_connection()                                                              
    cursor = conn.cursor()                                                                  
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))                            
    conn.commit()                                                                           
    conn.close()                                                                            
    print("🗑️ User deleted.")                                                                                                                                           

    conn = create_connection()
    cursor = conn.cursor()
