class vector:
    def __init__(self,a):
        self.A=a
        self.sum=[0, 0, 0]
    def __add__(self,other):
        for i in range(len(self.A)):
            self.sum[i]=self.A[i]+other.A[i]
        return self.sum

obj1=vector([1,2,3])
obj2=vector([0,3,4])
print(obj1+obj2)
