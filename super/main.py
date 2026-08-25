# super()                            - it is a function that is used to call methods of the parent class from the subclass.
#                                    - efficient to expand the functionality of a method

import math

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        if self.is_filled is True:
            print(f"It is {self.color} and is filled.")
        else:
            print(f"It is {self.color} and is not filled.")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"This is a {self.color} circle with an area of {math.pi * pow(self.radius, 2)}cm^2")
        print()


class Square(Shape):
    def __init__(self, color, is_filled, length):
        super().__init__(color, is_filled)
        self.length = length

    def describe(self):
        super().describe()
        print(f"This is a {self.color} square with an area of {round(pow(self.length, 2))}cm^2")
        print()

class Rectangle(Shape):
    def __init__(self, color, is_filled, length, breadth):
        super().__init__(color, is_filled)
        self.length = length
        self.breadth = breadth

    def describe(self):
        super().describe()
        print(f"This is a {self.color} rectangle with an area of {self.length*self.breadth}cm^2")

circle = Circle("Red", True, 5)
square = Square("Blue", False, 25)
rectangle = Rectangle("Yellow", True, 5, 8)


circle.describe()
square.describe()
rectangle.describe()