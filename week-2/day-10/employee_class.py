# python program to demonstrate inheritance with Employee and Manager classes

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def work(self):
        return f"{self.name} is working as a {self.position}. His salary is {self.salary}."

class Manager(Employee):
    def __init__(self, name, position, salary, department):
        super().__init__(name, position, salary)
        self.department = department

    def manage_team(self):
        return f"{self.name} is managing the {self.department} department."
    

emp = Employee("John Doe", "Developer", 60000)
mgr = Manager("Jane Smith", "Manager", 80000, "IT")

print(emp.work())  # John Doe is working as a Developer.
print(mgr.work())  # Jane Smith is working as a Manager.
print(mgr.manage_team())  # Jane Smith is managing the IT department.