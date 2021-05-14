import math
class Shape:
    def area(self):
        pass
    def display(self):
        pass

class circle(Shape):
    def __init__(self):
        self.r=eval(input("Enter radius of Circle:\n"))
        self.a=0
    def area(self):
        self.a=2* math.pi * self.r**2
    def display(self):
        print(self.a)
        

class rectangle(Shape):
    def __init__(self):
        self.l=eval(input("Enter length of Rectangle:\n"))
        self.b=eval(input("Enter breadth of Rectangle:\n"))
        self.a=0
    def area(self):
        self.a=self.l*self.b
    def display(self):
        print(self.a)

class square(Shape):
    def __init__(self):
        self.s=eval(input("Enter length of side of Square:\n"))
        self.a=0
    def area(self):
        self.a=self.s**2
    def display(self):
        print(self.a)

class triangle(Shape):
    def __init__(self):
        self.s=eval(input("Enter length of side of Triangle:\n"))
        self.a=0
    def area(self):
        self.a=(math.sqrt(3)/4)*self.s**2
    def display(self):
        print(self.a)

c=circle()
c.area()
c.display()

r=rectangle()
r.area()
r.display()

s=square()
s.area()
s.display()

t=triangle()
t.area()
t.display()
