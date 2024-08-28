# first line of code
print("Hello!")

""" end uses for printing code in same line """
print("Hey Hello!,", end=" ")
print("I am a QA engineer.", end=" ")
print("started Learning python.")

print("Variables")
# Variables - no need to specify the data types
a = 10
b = "Pavan Kalyan"
c = True
d = 2.4
e = 'Hello!'
print(a)
print(b)
print(c)
print(d)
print(e)

print("-------")
a = 7
A = 24
print(a)
print(A)

print("--------")
x = y = z = 3
print(x, y, z)

print("--------")
my_first_name = "Pavan"
my_last_name = "Kalyan"
print("My name is", my_first_name, my_last_name)

print("type()")
# Using type() for finding the data types of the variable
# Data types - Int, String, Float, Boolean, Dictionary, Tuple, List
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print("Type casting")
# Float to integer
float_num = 3.14
int_num = int(float_num)
print(int_num)

# String to integer
str_num = "100"
int_num = int(str_num)
print(int_num)

# Integer to String
int_num = 10
str_num = str(int_num)
print(str_num)

# Float to String
float_num = 1.4141
str_num = str(float_num)
print(str_num)

# Integer to float
int_num = 4
float_num = float(int_num)
print(float_num)

# String to float
str_num = "90"
float_num = float(str_num)
print(float_num)

# String to list
str_val = "Hello"
list_val = list(str_val)
print(list_val)

# Tuple to list
tuple_val = (1, 2, 3)
list_val = list(tuple_val)
print(list_val)

# List to tuple
list_val = [1, 2, 3]
tuple_val = tuple(list_val)
print(tuple_val)

# List to set
list_val = [1, 2, 2, 3]
set_val = set(list_val)
print(set_val)

print("# Operators")
print("# Arithmetic operators")
a = 10
b = 5
print(a + b)  # 15
print(a - b)  # 5
print(a * b)  # 50
print(a / b)  # 2
print(a % b)  # 0
print(a ** b)  # 100000
print(a // b)  # 2 floor division(//) - returns output without decimals

print("# Assignment operators")
a += b  # a = a + b
print(a)  # 15
a -= b  # 15 - 5 = 10
print(a)  # 10
a *= b  # 10 * 5
print(a)  # 50
a /= b  # 50 / 5 = 10
print(a)  # 10

print("# Relational operators")
print(a > b)  # True
print(a < b)  # False
print(a >= b)  # True
print(a <= b)  # False
print(a != b)  # True
print(a == b)  # False

print("# Logical operators")
print(a > b and a < b)  # True and False => False
print(a > b or a < b)  # True or False => True
print(not a > b)  # not True => False

# Deleting a  variable
# del variable => del a => it deletes the variable a

# Using + sign for string concatenation
print("Pavan" + " " + "Kalyan")  # Str + Str
print("DOB: " + str(24))  # Str + int (converted into string)
print("DOB:", 6)  # String + int (By using comma, Concatenating is possible with text and number)

# Multi-line preformatted string text
string = """Fallen cold and dead. 
O Captain! my Captain! 
rise up and hear the bells;. 
Rise up—for you the flag is flung—for you the bugle ..."""
print(string)

# Control flow - selection/decision control statements
print("# If condition")
a = 10
b = 7
if a > b:
    print(a, "is greater than", b)
print("End")

print("# If-else condition")
a = 10
b = 7
if a < b:
    print(a, "is greater than", b)
else:
    print("{0} is less than {1}".format(a, b))
print("End")

print("# If-elif-else condition")
a, b, c, d = 2, 3, 4, 5
if a > b:
    print(a, "is greater than", b)
elif b < c:
    print(b, "is less than", c)
elif c > d:
    print(c, "is greater than", d)
else:
    print(a, "is less than", b, b, "is less than", c, c, "is less than", d)
print("End")

# Loop / iterative statements
print("While loop")
i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print("loop ends when i value is greater than 10:", i)
print("End.")

# for loop statement
print("for loop")
for i in range(3):
    print(i)
print("-------")

for i in range(1, 10):
    print(i)
print("-------")

# 3rd range value indicates that it's addition to the range value, where 1 + 2 => 3, and then 3 + 2 => 5, till range of 10.
for i in range(1, 10, 2):
    print(i)

# Transfer/Jump statements
# break and continue
print("break and continue")
for i in range(10):
    if i == 5:
        break
    print(i)
print("breaks the iteration when the condition is satisfied.")

for i in range(10):
    if i == 5:
        continue
    print(i)
print("Skips the iteration when condition is satisfied.")

print("While loop - continue")
i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1
print("Skips the iteration when condition is satisfied.")

print("While loop - break")
i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1
print("breaks the iteration when the condition is satisfied.")

print("-----------------------------------------------------------------")


# Function
# format of a function to be called with def word first and then function name in snake case.
def my_first_function():
    print("Yeah, it's the first function")


my_first_function()
# calling the function, We can call the same function multiple times.
my_first_function()


# Parametirizing the functions
def my_first_name(name):
    print("my first name:" + name)


my_first_name("Pavan")
my_first_name("Che")


# Default Arguments in function
def my_last_name(name="Kalyan"):
    print("my last name:" + name)


my_last_name()  #default argument passed.
my_last_name("CHE")  # Passing arguments, so the current argument prints.


# Function with multiple parameters
def sum(a, b, c):
    print("sum of the values {0},{1},{2} is".format(a, b, c), (a + b + c))


sum(2, 3, 4)
sum(4, 5, 6)


# Functions can return data
def sum(a, b):
    return a + b  # it returns the data


print(sum(2, 3))

# Collecting input from user using input() built-in function
"""
print("Enter your name:")
my_first_name = input()
print("Welcome! " + my_first_name)

print("--------")
print("first number:")
num1 = input()
print("second number:")
num2 = input()
# Convert the inputs to integers and calculate the sum
sum_result = int(num1) + int(num2)
# Print the result
print("sum of num1 and num2: " + str(sum_result)) """

# max() and min() in-built functions
values = (1, 2, 4, 5, 8)
print("max value:", max(values))
print("min value:", min(values))

print("Local and Global variables:")
# Local and Global variable
f_name = "Pavan"  # global variable: called directly within the file and outside the function


def my_name():
    global l_name  # declaring local variable globally
    l_name = "Kalyan"  #Local vraiable: called directly inside the function
    print("first name: " + f_name)
    print("last name: " + l_name)


my_name()  # calling both global and local here
print("first name: " + f_name)  # calling global variable here
print("last name: " + l_name)


# Pass statement - for future implementations
def sum():
    pass


if 5 > 3:
    pass

for i in range(1, 10):
    pass
# it'll not throw any error, simply ignore the function


# Collections - which allows multiple values to store in a single variable.
# Data Types - List, Tuple, Dictionary, set
# List
colors = ["Yellow", "Blue", "Red", "Green", "White", "Black"]
# len(): prints the length of list, starts from 0.
print(len(colors))
for i in range(len(colors)):
    print(colors[i])

a = [1, 8, 9, 10, 4, 7]
# append: adds the value to the end of list
a.append(3)
print(a)
# insert: inserts the value next to index value taken
a.insert(5, 5)
print(a)

# remove(): Removing the element from the list
a.remove(10)
print(a)

# pop(): Removes last element from the list
a.pop()
print(a)

# Removing element by using their index
a.pop(2)
print(a)

# clear(): Remove all the elements in the list
a.clear()
print(a)

# reverse(): reverse elements
colors.reverse()
print(colors)

# sort(): sorts the elements
colors.sort()
print(colors)

# index(): returns index of elements in the list
index_color = colors.index("White")
print(index_color)

# Nested list
b = [1, [2, 3, 4], 5, 6, 7]
print(b[1][2])

# it can store different types of data
specifications = ["Triumph", "600cc", 45.9, 650000, True]
print(specifications[0])

# Forward and Backward index
c = [3, 4, 5, 6, 8, 8, 32, 2, 4, 5, 31]
print(c[4])  # Forward index => 8
print(len(c))  # 11
print(c[-2])  # Backward index = -2 + length of index => -2 + 11 => 9

# Slicing lists
print(c[2:5])  # index:position
print(c[:4])  # index 0: position 4
print(c[1:])  # index 1: last position
print(c[:])  # index 0: last position

# count() : counts the element in the list
print(c.count(8))

# max and min
print(max(c))
print(min(c))

# sum
k = [9, 3, 4, 5, 7, 8, 9]
# print(sum(k))

# type
print(type(k))

# delete
del k

# finding element present in the list or not, returns True or False.
k = [2, 4, 5, 6, 7, 8, 9, 0]
print(5 in k)  # Ture
print(1 in k)  # False

# concat
print(c + k)
print(len(c + k))

# Extend list
l = [1, 2, 3]
m = [7, 5, 8]
l.extend(m)  # This modifies l in place
print(l)  # This will print the extended list l
print(m)  # This will print the original list m

# Tuple - using ()
"""Immutable - can't be modified or updated.
Where list is mutable - it can be modified or updated. """
t = (1, 2, 3, 4, 5)
print(t)
print(type(t))
print(t[3])  # 4
print(len(t))

# Set - using {}
"""Set is mutable - can edit and modify.
No indexing
Random order
Duplicates not allowed."""
s = {1, 6, 7, 9, 2, 5}
print(s)
print(type(s))
print(len(s))
# adds element to the set
s.add(3)
print(s)

# add multiple values to the set
s.update([8, 4])
print(s)

# removes random element to the list
s.pop()
print(s)

# Union
a = {1, 3, 7, 9, 11}
b = {2, 4, 6, 8, 9, 10}
print(a.union(b))
print(a | b)

# Intersection
print(a.intersection(b))
print(a & b)

# Difference
print(a.difference(b))
print(a - b)

# Symmetric difference
print(a.symmetric_difference(b))
print(a ^ b)

print(min(a))
print(max(a))

# Dictionary : consists of key, value pairs
Bike = {"Brand": "Triumph",
        "Model": "BMW R 1250 GS",
        "Price": 2055000}
print(Bike)

# returns keys and values
print(Bike.keys())
print(Bike.values())

# Get values by get in-built command
print(Bike.get("Brand"))
print(Bike["Model"])

# Add new key and value pairs
Bike["color"] = "White"
print(Bike)

# Update
Bike["color"] = "Blue"
print(Bike)

# For-range loop
for k in Bike.keys():
    print(k)  # return keys
for v in Bike.values():
    print(v)  # return values
for k, v in Bike.items():
    print(k, v)  # returns key and values

del Bike["color"]  # deletes the key, value pair from dictionary
print(Bike)

print(len(Bike))  # length

# del Bike - Deletes the dictionary

Bike.pop("Price")  # removes the key, value
print(Bike)

Bike.clear()  # clears dictionary
print(Bike)

# Strings
first_name = "Pavan Kalyan"
print(first_name)
print(first_name.upper())
print(first_name.lower())
print(len(first_name))
print(first_name.capitalize())
print(first_name.casefold())
print(first_name.count("Kalyan"))
print((first_name.replace("k", "K")))

# File Handling
file = open("C:\\PycharmProjects\\PythonProject\\Files\\sampleFile.txt", "w")
file.write("Hey Hi! \n")
file.write("My name is Che")
# print(file.read())
file.close()

"""
w - write
r - read only
a - appending
"""

sum = lambda a,b : a+b
print(sum(92,3))