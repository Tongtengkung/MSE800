from database import create_connection
import sqlite3

def add_course(name, unit):                                                             #ฟังก์ชันสำหรับเพิ่มข้อมูลลงในตาราง course
    conn = create_connection()                                                              #สร้างการเชื่อมต่อกับฐานข้อมูล
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO course (name, unit) VALUES (?, ?)", (name, unit))      #ใช้สำหรับการเพิ่มข้อมูลลงในตาราง users
        conn.commit()                                                                       #ใช้สำหรับการบันทึกการเปลี่ยนแปลงในฐานข้อมูล
        print(" User added successfully.")                                                  #แสดงข้อความเมื่อเพิ่มข้อมูลสำเร็จ
    except sqlite3.IntegrityError:                                                          #ใช้สำหรับการจัดการข้อผิดพลาดที่เกิดจากการละเมิดความสมบูรณ์ของข้อมูล
        print(" Email must be unique.")                                                     #แสดงข้อความเมื่ออีเมลซ้ำ
    conn.close()
    
def view_courses():
    conn = create_connection()                                                              #สร้างการเชื่อมต่อกับฐานข้อมูล
    cursor = conn.cursor()                                                                  #ใช้สำหรับการสร้าง cursor object
    cursor.execute("SELECT * FROM courses")                                                 #ใช้สำหรับการดึงข้อมูลทั้งหมดจากตาราง users
    rows = cursor.fetchall()                                                                #ใช้สำหรับการดึงข้อมูลทั้งหมดจาก cursor object
    conn.close()                                                                            #ปิดการเชื่อมต่อกับฐานข้อมูล
    return rows                                                                             #ส่งค่าข้อมูลทั้งหมดกลับไปยังฟังก์ชันที่เรียกใช้       