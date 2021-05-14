from math import *
class circle:
    def __init__(self):
        self.r=0
        self.area=0
        self.circum=0
    def calc(self):
        self.r=eval(input("Enter radius:\n"))
        self.area=pi*self.r*self.r
        self.circum=2*pi*self.r
    def disp(self):
        print("Area of circle:",self.area)
        print("Circumference of circle:",self.circum)
obj=circle()
obj.calc()
obj.disp()
