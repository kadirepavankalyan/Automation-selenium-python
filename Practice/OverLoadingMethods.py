class A:
    def sample_method(self, A=None, B=None):
        if A is not None and B is not None:
            print(A * B)
        elif A is not None:
            print(A)
        else:
            print("Nothing")


obj = A()
obj.sample_method(2, 4)  # Both A and B are provided; prints 8
obj.sample_method(5)           # Only A is provided; prints 5
obj.sample_method()            # Neither A nor B are provided; prints "Nothing"
