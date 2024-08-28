# Single Level Inheritance
class A:
    A = 10


class B(A):
    B = 20


obj = B()
print("Single level inheritance:")
print("obj.A:", obj.A)  # Inherited from class A
print("obj.B:", obj.B)  # Defined in class B


# Multi-Level Inheritance
class A:
    A = 10


class B(A):
    B = 20


class C(B):
    C = 30


obj1 = B()
print("\nMulti-level inheritance:")
print("obj1.B:", obj1.B)  # Defined in class B
print("obj1.A:", obj1.A)  # Inherited from class A

obj2 = C()
print("obj2.C:", obj2.C)  # Defined in class C
print("obj2.B:", obj2.B)  # Inherited from class B
print("obj2.A:", obj2.A)  # Inherited from class A


# Hierarchical Inheritance
class A:
    A = 10


class B(A):
    B = 20


class C(B):
    C = 30


obj3 = C()
print("\nHierarchical inheritance:")
print("obj3.C:", obj3.C)  # Defined in class C
print("obj3.B:", obj3.B)  # Inherited from class B
print("obj3.A:", obj3.A)  # Inherited from class A

obj4 = B()
print("obj4.B:", obj4.B)  # Defined in class B
print("obj4.A:", obj4.A)  # Inherited from class A


# Multiple Inheritance
class A:
    A = 10


class B:
    B = 20


class C(A, B):
    C = 30


obj5 = C()
print("\nMultiple inheritance:")
print("obj5.C:", obj5.C)  # Defined in class C
print("obj5.B:", obj5.B)  # Inherited from class B
print("obj5.A:", obj5.A)  # Inherited from class A


# Hybrid Inheritance: Hierarchical + Multiple
class A:
    A = 10


class B(A):
    B = 20


class C(A):
    C = 30


class D(B, C):
    D = 40


obj6 = D()
print("\nHybrid Inheritance:")
print("obj6.D: ", obj6.D)  # Defined in class D
print("obj6.C: ", obj6.C)  # Inherited from class C
print("obj6.B: ", obj6.B)  # Inherited from class B
print("obj6.A: ", obj6.A)  # Inherited from class A

"""
Single-Level Inheritance:
Class B inherits from class A.
An instance of B can access both its own variable B and the inherited variable A.

Multi-Level Inheritance: 
Class C inherits from class B, which in turn inherits from class A.
An instance of C can access variables from all three classes.

Hierarchical Inheritance: two child classes have same parent class.
Multiple classes (B and C) inherit from the same parent class A.
An instance of B or C can access the inherited variables from class A.

Multiple Inheritance: A child class has two parent classes.
Class C inherits from both classes A and B.
An instance of C can access variables from both A and B.

Hybrid Inheritance:
Class A is the base class.
Classes B and C inherit from class A (hierarchical inheritance).
Class D inherits from both B and C (multiple inheritance).
An instance of class D can access variables from all its parent classes: D, C, B, and A.
"""
