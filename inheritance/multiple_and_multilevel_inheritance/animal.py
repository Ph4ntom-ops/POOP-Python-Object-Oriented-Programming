class Animal:
    def __init__(self, name):
        self.name = name

    def sleep(self):
        print(f"{self.name} is asleep")

    def eat(self):
        print(f"{self.name} is eating")

class Prey(Animal):
    def run(self):
        print(f"{self.name} is running.")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting.")

class Mixed(Prey, Predator):
    pass

rabbit = Prey("Dante")
tiger = Predator("Rocky")
fish = Mixed("Aizen")

rabbit.eat()
rabbit.sleep()
rabbit.run()

print()

tiger.eat()
tiger.sleep()
tiger.hunt()

print()

fish.eat()
fish.sleep()
fish.hunt()
fish.run()