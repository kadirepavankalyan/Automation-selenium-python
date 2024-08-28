import math
import random

from Practice import Calculator

obj1 = Calculator.A()
obj1.addition(2,4)
obj1.substraction(4,2)

obj2 = Calculator.B()
obj2.division(2,4)
obj2.multiplication(4,6)

print("square root of ", math.sqrt(89768))
print("pi value: ",math.pi)
print(math.floor(83.398))

colors = ["Blue", "White", "Black"]
print(random.choice(colors))