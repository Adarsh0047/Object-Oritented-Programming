class CEO():
    def display(self):
        print("I am the CEO of the company")

class ProjectManager(CEO):
    def display(self):
        print("I am the Project Manager")

class TeamLeader(ProjectManager):
    def display(self):
        print("I am the Team Leader")

class Programmer(TeamLeader):
    def display(self):
        print("I am the programmer")

ce=CEO()
ce.display()
pm=ProjectManager()
pm.display()
tl=TeamLeader()
tl.display()
pr=Programmer()
pr.display()

