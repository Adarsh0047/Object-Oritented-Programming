class Division:
    a=0
    b=0
    def divide(self,x,y):
        self.a=x
        self.b=y
        return(x/y)
obj=Division()
c=obj.divide(12,6)
print(c)
