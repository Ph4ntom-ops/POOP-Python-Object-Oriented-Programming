# staticmethods                    - static methods are class methods that doesn't need 
#                                    an object to be instanciated. These methods are used
#                                    for general utility purposes that doesn't need access
#                                    to class data.

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def describe(self):
        return f"{self.name}: {self.position}"

    @staticmethod
    def is_valid_position(position):
        positions = ["Manager", "Scientist", "Cashier", "CEO"]
        return "This a valid position" if position in positions else "This is an invalid position"
    
employee1 = Employee("Spongebob", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Harry", "Wizard")
employee4 = Employee("Doraemon", "CEO")

print(Employee.is_valid_position(employee1.position))
print(Employee.is_valid_position(employee2.position))
print(Employee.is_valid_position(employee3.position))
print(Employee.is_valid_position(employee4.position))

print(employee1.describe())
print(employee2.describe())
print(employee3.describe())
print(employee4.describe())
