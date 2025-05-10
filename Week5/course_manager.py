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