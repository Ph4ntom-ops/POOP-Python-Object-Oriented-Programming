# ducktyping                                      - It is an another method to achieve polymorphism
#                                                 - If it acts like a duck and quacks like a duck, then it must be a duck.


class Animal:
    is_alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")
    
class Cat(Animal):
    def speak(self):
        print("MEOW")

class Car:
    is_alive = False
    def speak(self):
        print("HONK!")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.is_alive)
