class Addition:
    a=0
    b=0
    def add(Self,x,y):
        Self.a=x
        Self.b=y
        return(Self.a+Self.b)

obj=Addition()
c=obj.add(5,5)
print("Addition:",c)
