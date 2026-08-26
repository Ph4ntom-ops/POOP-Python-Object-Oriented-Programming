# Nested Class                         - It means one class inside another class
#                                       class A:
#                                           class B:
#                                               ...


class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position
        
        def describe(self):
            return f"{self.name} is a {self.position}."
    
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []
    
    def add_employees(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)
    
    def list_employees(self):
        return [employee.describe() for employee in self.employees]

company = Company("The Ultimate Fake Company")

company.add_employees(name="Spongebob", position="Manager")
company.add_employees(name="Doraemon", position="Assistant")
company.add_employees(name="Nobita", position="Scientist")
company.add_employees(name="Suneo", position="CEO")

for employee in company.list_employees():
    print(employee)