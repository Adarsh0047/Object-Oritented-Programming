class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def printlist(self):
        tmp=self.head
        while (tmp):
            print(tmp.data)
            tmp=tmp.next
            if tmp.next==self.head:
                print(tmp.data)
                break
    def push(self,data):
        new_node=Node(data)
        if self.head == None:
            new_node.next=self.head
            self.head=new_node
            return
        last=self.head
        while last.next!=None:
            last=last.next
        last.next=new_node
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
        new_node.next=self.head
        

llist=LinkedList()
llist.push(12)
llist.append(123)
llist.insert_after(llist.head,11)
llist.printlist()


