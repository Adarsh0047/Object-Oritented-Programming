class NaturalNumber:
    def __init__(self):
        a=0        
        self.x=0
        self.y=1
        self.count=0
        self.nth=0

class Fgenerator(NaturalNumber):
    
    print("Fibonacci Sequence:")
    def fib(self,n):
        while self.count<n:
            print(self.x)
            self.nth=self.x+self.y
            self.x=self.y
            self.y=self.nth
            self.count+=1
    

class SumFib(Fgenerator):
    def  Sum_of_Fib_Series(self,n):
        while self.count<n:
            self.nth=self.x+self.y
            self.x=self.y
            self.y=self.nth
            self.count+=1
        print("Sum of series:",(self.nth-1))

n=eval(input("Enter the number till which you want to find fibonacci series:\n"))
Fibonacci=Fgenerator()
Fibonacci.fib(n)
a=0
Sum=SumFib()
Sum.Sum_of_Fib_Series(n)


