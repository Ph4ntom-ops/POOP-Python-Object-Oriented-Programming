# property decorator                          - Used to define a method as a property. It allows a method to be accessed as an attribute.
#                                             - Add additional login when reading, writing, or deleting an attribute
#                                             - Gives you getter, setter, and a deleter method

class Student:
    def __init__(self, name, email, password):
        self._name = name
        self._email = email
        self._password = password

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @email.setter
    def email(self, new_email):
        self._email = new_email

    @name.deleter
    def name(self):
        del self._name
        print("Deleted student name successfully.")

    @email.deleter
    def email(self):
        del self._email
        print("Deleted student email successfully.")

student = Student("Henry", "henrypotter@gmail.com", "calendar")
student.name = "Harry"
print(student.name)
student.email = "harrypotter@gmail.com"
print(student.email)

del student.name
del student.email
