class A:
    def addition(self, a, b):
        sum = a + b
        print(sum)

    def substraction(self, a, b):
        sub = a - b
        print(sub)

class B:
    def multiplication(self, a, b):
        mul = a * b
        print(mul)

    def division(self, a, b):
        if b != 0:
            div = a / b
            print(div)
        else:
            print("Cannot divide by zero")
            return None
