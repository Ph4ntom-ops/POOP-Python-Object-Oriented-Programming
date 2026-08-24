class Animal:
    def __init__(self, name):
        self.name = name
        self.isalive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW")

class Tiger(Animal):
    def speak(self):
        print("ROAR")

dog = Dog("Jackie")
cat = Cat("Elizabeth")
tiger = Tiger("Rocky")

print(dog.name)
print(cat.name)
print(tiger.name)

dog.speak()
cat.speak()
tiger.speak()