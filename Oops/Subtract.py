class Subtraction:
    a=0
    b=0
    def subtract(self,x,y):
        self.a=x
        self.b=y
        return(x-y)
obj=Subtraction()
c=obj.subtract(7,6)
print(c)
