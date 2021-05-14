import math
class trigonometry:
    def __init__(self):
        self.answer=0
        self.thetha=0
    def calculator(self):
        pass
    def display(self):
        pass

    
class sin(trigonometry):
    def __init__(self):
        self.answer=eval(input("Enter the sine value to find Thetha: "))
        self.thetha=0
    def calculator(self):
        self.theta=math.asin(self.answer)
    def display(self):
        print(math.degrees(self.theta))


class cos(trigonometry):
    def __init__(self):
        self.answer=eval(input("Enter the cosine value to find Thetha: "))
        self.theta=0
    def calculator(self):
        self.theta=math.acos(self.answer)
    def display(self):
        print(math.degrees(self.theta))


class tan(trigonometry):
    def __init__(self):
        self.answer=eval(input("Enter the tangent value to find Thetha: "))
        self.theta=0
    def calculator(self):
        self.theta=math.atan(self.answer)
    def display(self):
        print(math.degrees(self.theta))


sin_=sin()
sin_.calculator()
sin_.display()
cos_=cos()
cos_.calculator()
cos_.display()
tan_=tan()
tan_.calculator()
tan_.display()
