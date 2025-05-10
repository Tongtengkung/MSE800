from database import create_course_table
from course_manager import add_course, view_courses

def menu():
    print("\n==== Course Manager ====")
    print("1. Add Course")
    print("2. View All Courses")
    print("3. Search course by Name")
    print("4. Delete course by ID")
    print("5. Exit ")
    print("6. Advanced search based on ID and name")

def main():
    create_course_table()                                                                                      
    while True:
        menu()
        choice = input("Select an option (1-6): ")
        if choice == '1':
            name = input("Enter name: ")
            unit = input("Enter unit: ")
            add_course(name, unit)

        elif choice == '2':
            courses = view_courses()
            for course in courses:
                print(course)
        
        elif choice == '5':
            print("Goodbye!")
            break
                                                                  

if __name__ == "__main__":                                                      #ฟังก์ชันหลักที่ใช้ในการเรียกใช้งานโปรแกรม
    main()
