# classmethod                              - It's a type of method that is directly used by the class 
#                                            and is used for modifying the class variables.


class Student:
    total_students = 0
    total_gpa = 0
    
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.total_students += 1
        Student.total_gpa += gpa
    
    def describe(self):
        return f"{self.name} scored {self.gpa}GPA"
    
    @classmethod
    def num_of_students(cls):
        return cls.total_students
        
    @classmethod
    def average_gpa(cls):
        return 0 if cls.total_students == 0 else f"Average GPA: {cls.total_gpa / cls.total_students:.2f}"

student1 = Student("Squidward", 3.55)
student2 = Student("Spongebob", 3.7)
student3 = Student("Digisuki", 3.9)
student4 = Student("Nobita", 4)

print(f"There are {Student.num_of_students()} students.")
print(Student.average_gpa())