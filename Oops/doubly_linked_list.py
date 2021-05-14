class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Link():
    def __init__(self):
        self.head=None
    def push(self,new_node):
        new_node=Node(new_node)
        new_node.next=self.head
        self.head=new_node
        new_node.prev=None
    def add_mid(self,prev_node,new_node):
        if prev_node is None:
            print("No such node")
            return
        new_node=Node(new_node)
        new_node.next=prev_node.next
        prev_node.next=new_node
        new_node.prev=prev_node
        if new_node.next is not None:
            new_node.next.prev=new_node
    def append(self,new_node):
        last=self.head
        new_node=Node(new_node)
        while(last.next):
            last=last.next
        last.next=new_node
        new_node.prev=last
    def printlist(self):
        tmp=self.head
        while(tmp):
            print(tmp.data)
            tmp=tmp.next

llist=Link()
llist.push(0)
llist.push(1)
llist.add_mid(llist.head,5)
llist.append(7)
llist.printlist()
