# Encapsulation - wrapping data(i.e, variables) and code(i.e, Methods) together in a single unit.
"""
Encapsulation is a fundamental concept in object-oriented programming (OOP) that refers to the
bundling of data (attributes) and methods (functions) that operate on that data into a single unit,
or class.
    It also involves restricting direct access to some of an object's components, which can prevent the
accidental modification of data. This is typically achieved through access modifiers like private, protected,
and public.
"""
class A:
    __age = 0  # Private class attribute

    def set_age(self, age):
        A.__age = age  # Setting the value of the private class attribute

    def get_age(self):
        return A.__age  # Getting the value of the private class attribute


obj = A()
obj.set_age(30)
print(obj.get_age())