from database import create_course_table
from course_manager import add_course

def menu():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. Exit ")
    print("6. Advanced search based on ID and name")
    print("7. Add Course")

def main():
    create_course_table()                                                                                      
    while True:
        menu()
        choice = input("Select an option (1-6): ")
        if choice == '1':
            name = input("Enter name: ")
            unit = input("Enter unit: ")
            add_course(name, unit)
        
        elif choice == '5':
            print("Goodbye!")
            break
                                                                  

if __name__ == "__main__":                                                      #ฟังก์ชันหลักที่ใช้ในการเรียกใช้งานโปรแกรม
    main()
