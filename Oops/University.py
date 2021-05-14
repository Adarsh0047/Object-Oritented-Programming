class University:
    def __init__(self):
        self.days=1
        self.salary_e=0
        self.salary=0
        self.leave=0
        self.overtime=0
    def salaryTransaction(self):
        self.days=eval(input("Enter number of working days:\t"))
        self.salary_e=1800*self.days
        self.leave=eval(input("Enter Number of holidays you have taken in numbers:\t"))
        self.salary=self.salary_e-(2500*self.leave)
        self.overtime=eval(input("Enter number of overtime hours worked in numbers:\t"))
        self.salary=self.salary_e+(300*self.overtime)
    def display(self):
        print("The salary eligible is :\t",self.salary)
        print ("Number of holidays:\t",self.leave,"\tdays.")
        print("Overtime:\t",self.overtime,"\tdays.")

class Faculty(University):      
    def display(self):
        print("The gross eligible salary is:\t",self.salary_e)
        print ("Number of holidays:\t",self.leave,"\tdays.")
        print("Overtime:\t",self.overtime,"\thrs.")
        print("The net salary is:\t",self.salary)

class Student(University):    
    def display(self):
        print("The gross eligible salary is: Not eligible")
        print ("Number of holidays:Not eligible")
        print("Overtime:Not eligible")
        print("The net salary is:Not eligible")

class NonTeaching_Faculty(University):        
    def display(self):
        print("The gross eligible salary is:\t",self.salary_e)
        print ("Number of holidays:\t",self.leave,"\tdays.")
        print("Overtime:\t",self.overtime,"\thrs.")
        print("The net salary is:\t",self.salary)

faculty=Faculty()
faculty.salaryTransaction()
faculty.display()

student=Student()
student.salaryTransaction()
student.display()

NtFaculty=NonTeaching_Faculty()
NtFaculty.salaryTransaction()
NtFaculty.display()
        
