class Multiplication:
    a=0
    b=0
    def multiply(self,x,y):
        self.a=x
        self.b=y
        return(x*y)
obj=Multiplication()
c=obj.multiply(7,6)
print(c)
