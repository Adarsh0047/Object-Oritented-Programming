class RealNumber():
    def __init__(self):
        self.inp=0
        self.sum=0
        self.square=0
    def generate(self):
        self.inp=eval(input('Enter the number upto to which you want to generate series: '))
        for i in range(self.inp):
            print(i,end=' ')
        print('\n')
        return self.inp

class sumofSeries(RealNumber):
    def add(self,num):
        for i in range(num):
            self.sum+=i
        print(self.sum)

class SumofSquareSeries(RealNumber):
    def sq(self,num):
        for i in range(num):
            self.square=i**2+self.square
        print(self.square)
        
obj1=RealNumber()
obj2=sumofSeries()
obj3=SumofSquareSeries()
n=obj1.generate()
obj2.add(n)
obj3.sq(n)
