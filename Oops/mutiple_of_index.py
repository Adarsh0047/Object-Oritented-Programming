class indexing:
    def __init__(self):
        self.str=input("Enter the string:\n")
        self.k=eval(input("Enter K value:\n"))
        self.i=0

    def calc(self):
        for(self.i) in (self.str):
            if (self.str.index(self.i)+1)%self.k==0:
                print(self.i
                      )
            else:
                pass

obj=indexing()
obj.calc()
