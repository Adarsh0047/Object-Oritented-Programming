class Ranking:
    def __init__(self):
        self.rank=0
        self.inp_sent=""
        self.dict={}
        self.lis=[]
        self.leng=0
    def inp(self):
        self.inp_sent=input("Enter a sentence:\n")
        self.lis=self.inp_sent.split()
        self.leng=len(self.lis)
    def calculate(self) :
        for i in range(self.leng):
                self.rank=self.lis.count(self.lis[i])
                self.dict.update({self.lis[i]:self.rank})
        print(self.dict)
obj=Ranking()
obj.inp()
obj.calculate()
