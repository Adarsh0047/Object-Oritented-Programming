class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class LinkedList:
    def __init__(self):
        self.head=None
    def printlist(self):
        tmp=self.head
        while (tmp):
            print(tmp.data)
            tmp=tmp.next
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        
    def insert_after(self,prev_node,data):
        if prev_node is None:
            print("No such node")
        new_node=Node(data)
        new_node.next=prev_node.next
        prev_node.next=new_node
    def append(self,data):
        new_node=Node(data)
        last=self.head
        while(last.next):
            last=last.next
        last.next=new_node
    def dele_f(self):
        tmp=self.head
        self.head=tmp.next
        tmp=None
    def dele_midd(self,prev_node):
        if prev_node is None:
            print("No such node")
        elif prev_node.next is None:
            return
        
            
        tmp=prev_node.next
        if tmp.next is None:
            prev_node.next=None
        else:
            prev_node.next=tmp.next
        tmp=None
        
        

llist=LinkedList()
llist.push(1)
llist.append(9)
llist.insert_after(llist.head,11)
#llist.dele_midd(llist.head)
llist.printlist()


