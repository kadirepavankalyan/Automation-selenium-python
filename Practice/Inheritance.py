# Inheritance: Child class acquiring a property of parent class.
# Parent class
class A:
    varA = "Var A from class A"

    def method_A(self):
        print("method_A from class A")


# Child class inheriting from Parent class A
class B(A):
    varB = "Var B from class B"

    def method_B(self):
        print("method_B from class B")


# Creating an instance of class B
obj = B()

# Calling methods and accessing variables
obj.method_B()  # Calls method_B from class B
print(obj.varB)  # Accesses varB from class B
obj.method_A()  # Calls method_A from class A (inherited)
print(obj.varA)  # Accesses varA from class A (inherited)

"""
Inheritance: Class B inherits from class A, meaning B has access to the methods and variables of A.
Overriding and Accessing Parent Class Methods and Variables: An instance of class B can call methods and access variables defined in class A.
Creating Instances: An instance of the child class B can use both its own properties and methods, as well as those inherited from the parent class A.
"""