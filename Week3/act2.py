class   Student:
    def __init__(self, name, grade):
        self.students = []
        self.name = name
        self.grade = grade
        
    def add_student(self, name, grade):
        self.students.append((name, grade))

    def delete_student(self, name):
        for student in self.students:
            if student[0] == name:
                self.students.remove(student)
                break

    def update_student(self, name, new_grade):
        for student in self.students:
            if student[0] == name:
                index = self.students.index(student)
                self.students[index] = (name, new_grade)
                break

    def list_students(self):
        for student in self.students:
            print(f"Name: {student[0]}, Grade: {student[1]}")

print("Welcome to lovely class room!")

students = Student("", "")                                                   
while True:
    act = input("Please, enter the action (add, delete, list, update, exit): ")    
    if act == "add":
        for list, student in enumerate(students.students, start=1):
            print(f"Student {list}: {student}")
        name = input("Enter the student name: ")
        grade = input("Enter the student grade: ")
        students.add_student(name, grade)
        print(f"Student '{name}' added successfully.")

    elif act == "list":                                                    
        for list, student in enumerate(students.students, start=1):
            print(f"Student {list}: {student}")

    elif act == "delete":                                                  
        for list, student in enumerate(students.students, start=1):
            print(f"Student {list}: {student}")
        name = input("Enter the student name to delete: ")
        students.delete_student(name)
        print(f"Student '{name}' deleted successfully.")
    
    elif act == "update":
        for list, student in enumerate(students.students, start=1):
            print(f"Student {list}: {student}")
        name = input("Enter the student name to update: ")
        new_grade = input("Enter the new grade: ")
        students.update_student(name, new_grade)
        print(f"Student '{name}' updated successfully.")

    elif act == "exit":                                                    
        print("Exiting the program.")
        break

    else:                                                                   
        print("Invalid action. Please try again.")
            