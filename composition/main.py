# Composition                                    - It is the type of relationship where the composed object
#                                                  directly owns its component object. The component objects
#                                                  cannot work on their own.
#                                                  "owns-a" relationship


class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power
    
class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, make, year, model, horse_power, size):
        self.make = make
        self.year = year
        self.model = model
        self.engine = Engine(horse_power)
        self.wheel = [Wheel(size) for wheel in range(4)]
    
    def display_car(self):
        return f"{self.year} {self.make} {self.model} contains {self.engine.horse_power} and has {self.wheel[0].size}in tires."

car1 = Car("Aston Martin", 2022, "DB11", 630, 19)
car2 = Car("Audi", 2022, "RS Q8", 591, 18)
car3 = Car("Bently", 2021, "Bentagya", 542, 19)

cars = [car1, car2, car3]

for car in cars:
    print(car.display_car())

