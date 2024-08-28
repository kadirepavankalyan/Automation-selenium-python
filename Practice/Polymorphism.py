# Polymorphism - Method overriding
class A:
    a = 10

    def sample_method(self):
        print("sample method from class A")


class B(A):
    a = 20

    def sample_method(self):
        print("sample method from class B")


# Creating an instance of class B
obj = B()
print(obj.a)  # Accessing the overridden variable 'a' in class B
obj.sample_method()  # Calling the overridden method 'sample_method' in class B
