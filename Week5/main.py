from database import create_table
from user_manager import add_user, view_users, search_user, delete_user, advance_search_user
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
    create_table()                                                                                      
    while True:
        menu()
        choice = input("Select an option (1-6): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '5':
            print("Goodbye!")
            break
        elif choice == '6':
            name = input("Enter name to search: ")
            user_id = int(input("Enter user ID to search: "))
            users = advance_search_user(name,user_id)                                                             
            print(user)

        elif choice == '7':
            course_id = int(input("Enter course ID: "))
            name = input("Enter course name: ")
            unit = int(input("Enter course unit: "))
            add_course(course_id, name, unit)                                                             

if __name__ == "__main__":              #ฟังก์ชันหลักที่ใช้ในการเรียกใช้งานโปรแกรม
    main()
