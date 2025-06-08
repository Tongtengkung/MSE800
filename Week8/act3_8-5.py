class Company:                                          # Define a base class for Company (parent class)
    def __init__(self, name):
        self.name = name

    def company_info(self):
        print(f"Company: {self.name}")

class Employee(Company):                                # Employee class inherits from Company 
    def __init__(self, name, emp_id, department):
        super().__init__(name)
        self.emp_id = emp_id
        self.department = department

    def employee_info(self):
        print(f"Employee ID: {self.emp_id}, Department: {self.department}")

class Developer(Employee):                              # Developer class inherits from Employee      
    def __init__(self, name, emp_id, department, language):
        super().__init__(name, emp_id, department)
        self.language = language

    def developer_info(self):
        print(f"Programming Language: {self.language}")

class AIEngineer(Developer):                            # AIEngineer class inherits from Developer
    def __init__(self, name, emp_id, department, language, ml_framework):
        super().__init__(name, emp_id, department, language)
        self.ml_framework = ml_framework

    def ai_engineer_info(self):
        print(f"Uses ML Framework: {self.ml_framework}")

engineer = AIEngineer("OpenAI Inc.", 1024, "R&D", "Python", "TensorFlow")

engineer.company_info()
engineer.employee_info()
engineer.developer_info()
engineer.ai_engineer_info()

# So, this is the multilevel inheritance example:
# Company -> Employee -> Developer -> AIEngineer
# The AIEngineer class inherits from Developer, which inherits from Employee, which in turn inherits from Company.
# This allows the AIEngineer class to access methods and properties from all the parent classes.
