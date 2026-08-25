# polymorphism                                   - A Greek word that means "many forms"
#                                                  poly: many, morph: form

#                                                  Polymorphism can be obtained in two ways
#                                                  1) Inheritance: An object could be treated as the same type as a parent class
#                                                  2) Ducktyping
from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):                        # Shape class has many forms or faces such as circle, rectangle, square, and pizza as well. 

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):                     # This is a Circle as well as a Shape. Hence, it has two forms.
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * pow(self.radius, 2)

class Square(Shape):                     # This is a Square as well as a Shape. Hence, it has two forms.
    def __init__(self, length):
        self.length = length

    def area(self):
        return pow(self.length, 2)

class Rectangle(Shape):                  # This is a Rectangle as well as a Shape. Hence, it has two forms.
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

# Pizza is not necessarily a shape, but it's a circle 
# so we can inherit from the Circle class, which inherits from the Shape class. 
# So, ultimately, pizza has 3 forms: pizza, circle, and a shape.

class Pizza(Circle): 
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping


shapes = [Circle(7), Square(8), Rectangle(9,10), Pizza("pepperoni", 11)]

for shape in shapes:
    print(round(shape.area()))
                                    