class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

car1 = Car("Toyota Supra", 2017, "Black", False)
car2 = Car("Lamborghini", 2018, "Green", True)
car3 = Car("Porche", 2006, "White", False)

print(car3.model)