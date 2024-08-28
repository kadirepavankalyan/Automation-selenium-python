class Car:
    # Static Variable
    wheels = 4

    # Instance Variables
    def __init__(self, brand, model, mileage, price):
        self.brand = brand
        self.model = model
        self.mileage = mileage
        self.price = price

    # Instance Method
    def start_car(self):
        print(self.brand + " started!")
        print("Wheels (from class): ", Car.wheels)

    # Static Method
    @staticmethod
    def static_method():
        print("Static method called")

    @staticmethod
    def car_wheels():
        print("Number of wheels:", Car.wheels)
        Car.static_method()


# Creating an instance of Car
Honda = Car("Honda", "ModelA", 15.5, 100000)
Honda.start_car()
print("Wheels:", Honda.wheels)
print("Model:", Honda.model)

print("Wheels (from class):", Car.wheels)
Car.car_wheels()

"""
Static Variable (wheels): Shared by all instances of the Car class.
Instance Variables (brand, model, mileage, price): Unique to each instance of the Car class.
Instance Method (start_car): Can access instance variables and is called on an instance of the Car class.
Static Methods (static_method and car_wheels): Do not access instance variables and can be called on the class itself.
"""