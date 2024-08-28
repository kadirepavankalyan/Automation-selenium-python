# Private variables and Methods - Can be accessed only within the class.
class A:
    __a = 10  # Private class attribute starts with __

    def __sample(self): # Private method with starts with __
        print("Private method inside class A")

    def sample_details(self):
        print(self.__a)  # Accessing private class attribute
        self.__sample()  # Calling private method


obj = A()
obj.sample_details()
