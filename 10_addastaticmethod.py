'''Write a class "calculator" capable of finding square,cube, and square root of a number.
    Add a static method in this problem  to greet the user with hello Program saved as 10 addastaticmethod.py'''

class Calculator:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

    def sqaureroot(self):
        print(f"The suarerroot is {self.n**1/2}")

    @staticmethod
    def hello():
        print("Hello there!")

a = Calculator(4)
a.hello()
a.square()
a.cube()
a.sqaureroot()
