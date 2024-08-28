# Objects and Class
"""
Objects - An object is an instance of a class. It is created based on the blueprint defined by the class.
        Each object can have its own values for the attributes defined in the class.
Class - A class is like a blueprint or template for creating objects.
        It defines a set of attributes and methods that the objects created from the class can have.
"""


class Car():
    mileage = 20.5
    cost = 100000

    # Method - a function inside a class
    def petrol_car(self):
        print("runs with petrol")

    def diesel_car(self):
        print("runs with diesel")

    def electrical_car(self):
        print(self.mileage)
        print("Electrical car")

# object creation
audi = Car()  # audi => object reference

audi.petrol_car()
print(audi.cost)
print(audi.mileage)
audi.electrical_car()