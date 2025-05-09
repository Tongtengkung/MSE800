from database import create_connection
import sqlite3

def add_user(name, email):
    conn = create_connection()                                                              #สร้างการเชื่อมต่อกับฐานข้อมูล
    cursor = conn.cursor()                                                                  #ใช้สำหรับการสร้าง cursor object
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))      #ใช้สำหรับการเพิ่มข้อมูลลงในตาราง users
        conn.commit()                                                                       #ใช้สำหรับการบันทึกการเปลี่ยนแปลงในฐานข้อมูล
        print(" User added successfully.")                                                  #แสดงข้อความเมื่อเพิ่มข้อมูลสำเร็จ
    except sqlite3.IntegrityError:                                                          #ใช้สำหรับการจัดการข้อผิดพลาดที่เกิดจากการละเมิดความสมบูรณ์ของข้อมูล
        print(" Email must be unique.")                                                     #แสดงข้อความเมื่ออีเมลซ้ำ
    conn.close()                                                                            #ปิดการเชื่อมต่อกับฐานข้อมูล

def view_users():
    conn = create_connection()                                                              #สร้างการเชื่อมต่อกับฐานข้อมูล
    cursor = conn.cursor()                                                                  #ใช้สำหรับการสร้าง cursor object
    cursor.execute("SELECT * FROM users")                                                   #ใช้สำหรับการดึงข้อมูลทั้งหมดจากตาราง users
    rows = cursor.fetchall()                                                                #ใช้สำหรับการดึงข้อมูลทั้งหมดจาก cursor object
    conn.close()                                                                            #ปิดการเชื่อมต่อกับฐานข้อมูล
    return rows                                                                             #ส่งค่าข้อมูลทั้งหมดกลับไปยังฟังก์ชันที่เรียกใช้

def search_user(name):                                                                      #ฟังก์ชันสำหรับค้นหาผู้ใช้ตามชื่อ
    conn = create_connection()                                                              #สร้างการเชื่อมต่อกับฐานข้อมูล
    cursor = conn.cursor()                                                                  #ใช้สำหรับการสร้าง cursor object
    cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + name + '%',))            #ใช้สำหรับการค้นหาผู้ใช้ตามชื่อ
    rows = cursor.fetchall()                                                                #ใช้สำหรับการดึงข้อมูลทั้งหมดจาก cursor object
    conn.close()                                                                            #ปิดการเชื่อมต่อกับฐานข้อมูล   
    return rows                                                                             #ส่งค่าข้อมูลทั้งหมดกลับไปยังฟังก์ชันที่เรียกใช้

def delete_user(user_id):                                                                   #ฟังก์ชันสำหรับลบผู้ใช้ตาม ID
    conn = create_connection()                                                              #สร้างการเชื่อมต่อกับฐานข้อมูล
    cursor = conn.cursor()                                                                  #ใช้สำหรับการสร้าง cursor object
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))                            #ใช้สำหรับการลบผู้ใช้ตาม ID
    conn.commit()                                                                           #ใช้สำหรับการบันทึกการเปลี่ยนแปลงในฐานข้อมูล
    conn.close()                                                                            #ปิดการเชื่อมต่อกับฐานข้อมูล
    print("🗑️ User deleted.")                                                               #แสดงข้อความเมื่อผู้ใช้ถูกลบสำเร็จ

def advance_search_user(name,user_id):                                                              #ฟังก์ชันสำหรับค้นหาผู้ใช้ตามชื่อและID
    conn = create_connection()                                                                      #สร้างการเชื่อมต่อกับฐานข้อมูล
    cursor = conn.cursor()                                                                          #ใช้สำหรับการสร้าง cursor object
    cursor.execute("SELECT * FROM users WHERE name LIKE ? AND id = ?", ('%' + name + '%', user_id)) #ใช้สำหรับการค้นหาผู้ใช้ตามชื่อและID
    rows = cursor.fetchall()                                                                        #ใช้สำหรับการดึงข้อมูลทั้งหมดจาก cursor object
    conn.close()                                                                                    #ปิดการเชื่อมต่อกับฐานข้อมูล   
    return rows                                                                                     #ส่งค่าข้อมูลทั้งหมดกลับไปยังฟังก์ชันที่เรียกใช้