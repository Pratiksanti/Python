class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
     super().__init__(name, age)
     self.emp_id = emp_id
     self.salary = salary




    def display_employee_info(self):
        self.display_person_info()
        print(f"Employee iD: {self.emp_id}")
        print(f"Salary: {self.salary}")

emp=Employee("Virat",34,18,15000000)
emp.display_employee_info()

