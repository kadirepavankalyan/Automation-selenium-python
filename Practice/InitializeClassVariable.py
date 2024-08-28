# Initializing class variables using methods
# We can use __init__(self)  in built method
class Bike:
    def __init__(self, brand, model, mileage):
        self.brand = brand
        self.model = model
        self.mileage = mileage

    def bike_start(self):
        print(self.model + " Started!")

    def bike_stop(self):
        print(self.model + " stopped.")

    def bike_details(self):
        print("Bike brand: " + self.brand)
        print("Bike model: " + self.model)
        print("Bike mileage: " + str(self.mileage))


triumph = Bike("Triumph", "1250 GC", 24.5)
triumph.bike_start()
triumph.bike_details()
triumph.bike_stop()

print("---------------")
yamaha =  Bike("Yamaha", "Yamaha R15 V4", 51.4)
yamaha.bike_start()
yamaha.bike_details()
yamaha.bike_stop()