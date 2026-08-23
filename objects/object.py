from car import Car

car1 = Car("Toyota Supra", 2017, "Black", False)
car2 = Car("Lamborghini", 2018, "Green", True)
car3 = Car("Porche", 2006, "White", False)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

print()

car1.drive()
car2.drive()
car3.drive()

print()

car1.describe()
car2.describe()
car3.describe()