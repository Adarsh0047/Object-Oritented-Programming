class replicate:
    def __init__(self,st):
        self.string=st
        self.num=0
    def __pow__(self,other):
        tmp=""
        for i in range(int(other.string)):
            tmp=tmp+self.string
        return tmp
obj1=replicate("Hi")
num="3"
obj2=replicate(num)
print(obj1**obj2)
