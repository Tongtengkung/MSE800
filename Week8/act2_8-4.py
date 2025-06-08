class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old."

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)                                 # Call the initializer of the parent class
        self.student_id = student_id

    def introduce(self):
        return f"{super().introduce()} and my student ID is {self.student_id}."
    

# Create a Student object
student = Student("John", 20, 1234)

# Call the introduce method
print(student.introduce())
