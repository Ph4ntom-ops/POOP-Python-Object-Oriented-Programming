# class variables                               - defined outside of the constructor
#                                               - allows access to all the objects


class Student:
    graduation_year = 2026
    num_of_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_of_students += 1

student1 = Student("Spongebob", 25)
student2 = Student("Goku", 30)
student3 = Student("Vegeta", 31)
student4 = Student("Gohan", 15)
student5 = Student("Bulma", 35)

print(f"My graduation year of {Student.graduation_year} has {Student.num_of_students} students:")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
print(student5.name)