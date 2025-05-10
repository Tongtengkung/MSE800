from database import create_course_table
from course_manager import add_course, view_courses, delete_course

def menu():
    print("\n==== Course Manager ====")
    print("1. Add Course")
    print("2. View All Courses")
    print("3. Delete course by ID")
    print("4. Exit ")

def main():
    create_course_table()                                                                                      
    while True:
        menu()
        choice = input("Select an option (1-4): ")
        if choice == '1':
            name = input("Enter name: ")
            unit = input("Enter unit: ")
            add_course(name, unit)

        elif choice == '2':
            courses = view_courses()
            for course in courses:
                print(course)
        
        elif choice == '3':
            course_id = int(input("Enter course to delete: "))
            delete_course(course_id)

        elif choice == '4':
            print("Goodbye!")
            break
                                                                  

if __name__ == "__main__":                                                      #ฟังก์ชันหลักที่ใช้ในการเรียกใช้งานโปรแกรม
    main()
