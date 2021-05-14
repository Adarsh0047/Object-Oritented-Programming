class Matrix:
    def __init__(self):
        self.A=[]
        self.B=[]
        self.add=[]
        self.row=0
        self.column=0
        self.prod=[]


class Madd(Matrix):
    def inpu(self):
        self.row=eval(input("Enter the number of rows in matrix A:\n"))
        self.column=eval(input("Enter number of columns in matrix A:\n"))
        print("Enter matrix A rowwise:")
        for i in range(self.row):
            r=[]
            for j in range(self.column):
                r.append(eval(input()))
            self.A.append(r)

        print("Enter the matrix B entries rowwise:")
        for i in range(self.row):
            r=[]
            z=[]
            for j in range(self.column):
                z.append(0)
                r.append(eval(input()))
            self.B.append(r)
            self.add.append(z)

    def disp(self):
        print("The Matrix A:")
        for i in range(self.row):
            for j in range(self.column):
                print(self.A[i][j], end=" ")

        print("\nThe Matrix B:")
        for i in range(self.row):
            for j in range(self.column):
                print(self.B[i][j], end=" ")

    def addd(self):
        for i in range(len(self.A)):
            for j in range(len(self.A[0])):
                self.add[i][j]=self.A[i][j]+self.B[i][j]
        print("\n",self.add)
        
class Mmul(Matrix):
    def inpu(self):
        self.row=eval(input("Enter the number of rows in matrix A:\n"))
        self.column=eval(input("Enter number of columns in matrix A:\n"))
        print("Enter matrix A rowwise:")
        for i in range(self.row):
            r=[]
            z=[]
            for j in range(self.column):
                z.append(0)
                r.append(eval(input()))
            self.prod.append(z)
            self.A.append(r)

        print("Enter the matrix B entries rowwise:")
        for i in range(self.row):
            r=[]
            for j in range(self.column):
                r.append(eval(input()))
            self.B.append(r)

    def disp(self):
        print("The Matrix A:")
        for i in range(self.row):
            for j in range(self.column):
                print(self.A[i][j], end=" ")

        print("\n The Matrix B")
        for i in range(self.row):
            for j in range(self.column):
                print(self.B[i][j], end=" ")

    def prodd(self):
        for i in range(len(self.A)):
            for j in range(len(self.B[0])):
                for k in range(len(self.B)):
                    self.prod[i][j]+=self.A[i][k]*self.B[k][j]
        print("\n",self.prod)

addition=Madd()
addition.inpu()
addition.disp()
addition.addd()
multi=Mmul()
multi.inpu()
multi.disp()
multi.prodd()
