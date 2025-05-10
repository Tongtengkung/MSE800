import sqlite3

def create_connection():                                                #ฟังก์ชันสำหรับสร้างการเชื่อมต่อกับฐานข้อมูล
    conn = sqlite3.connect("users.db")                                  #สร้างการเชื่อมต่อกับฐานข้อมูล users.db
    return conn                                                         #ส่งค่าการเชื่อมต่อกลับไปยังฟังก์ชันที่เรียกใช้

def create_table():                                                     #ฟังก์ชันสำหรับสร้างตารางในฐานข้อมูล
    conn = create_connection()                                          #สร้างการเชื่อมต่อกับฐานข้อมูล
    cursor = conn.cursor()                                              #ใช้สำหรับการสร้าง cursor object
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')

def create_course_table():                                              #ฟังก์ชันสำหรับสร้างตาราง course ในฐานข้อมูล
    conn = create_connection()                                          #สร้างการเชื่อมต่อกับฐานข้อมูล
    cursor = conn.cursor()                                              #ใช้สำหรับการสร้าง cursor object
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS course (
            course_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            unit INTEGER
        )
    ''')
    conn.commit()
    conn.close()
