from playsound3 import playsound

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
        playsound('./dog.mp3')


class Cat(Animal):
    def speak(self):
        print("MEOW")
        playsound('./cat.mp3')

class Tiger(Animal):
    def speak(self):
        print("ROAR")
        playsound('./tiger.mp3')

dog = Dog("Jackie")
cat = Cat("Elizabeth")
tiger = Tiger("Rocky")

print(dog.name)
print(cat.name)
print(tiger.name)

dog.speak()
cat.speak()
tiger.speak()