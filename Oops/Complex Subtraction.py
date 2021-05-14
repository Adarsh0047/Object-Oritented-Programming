class sum_complex:
    x1=0
    x2=0+0j
    def addComplex(Self, y1, y2):
        Self.x1=y1
        Self.x2=y2
        return Self.x1 - Self.x2
z1 = complex(2, 3)
z2 = complex(1, 2)
obj=sum_complex()
c=obj.addComplex(z1,z2)
print( "Addtion is : ",c )
