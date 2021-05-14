class over:
    def __init__(self, *args):
        if len(args)==0:
            print("Overloading with 0 args passed while creating instance of the class")
        elif len(args)==1:
            print("Overloading with 1 args passed while creating instance of the class")
            print(args[0])
        elif len(args)>=2:
            print("Overloading with %d args passed while creating instance of the class" %(len(args)))
            prod=1
            for i in range(len(args)):
                prod=prod*args[i]
            print(prod)
        
obj1=over()
obj2=over(2)
obj3=over(2,3)
