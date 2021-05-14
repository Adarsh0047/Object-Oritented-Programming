class Employee:
    def getInfo(self,salary,hr):
        self.salary=str(salary)
        self.hr=hr
    def addSal(self):
        if int(self.salary)<500:
            self.salary=str(int(self.salary)+100)
        else:
            pass
    def addWorkSal(self):
        self.salary="$"+self.salary
    def display(self):
        print(self.salary)
        print(self.hr,"hrs")

obj=Employee()
obj.getInfo(300,4)
obj.display()
obj.addSal()
obj.display()
obj.addWorkSal()
obj.display()
            
        
