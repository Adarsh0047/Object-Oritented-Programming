class sort:
    def __init__(self):
        self.str=input("Enter a string separated with hyphen:\n")
        self.list_str=[]
    def start_sort(self):
        self.list_str=self.str.split("-")
        self.list_str.sort()
        return "-".join(self.list_str)

obj=sort()
c=obj.start_sort()
print(c)
        
        
        
