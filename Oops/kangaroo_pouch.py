class Kangaroo:
    def __init__(self):
        self.pouch_contents=[]
    def put_in_pouch(self,item):
        self.pouch_contents.append(item)
        return self.pouch_contents
kanga=Kangaroo()
roo=Kangaroo()
roo.put_in_pouch("I am a baby Kangaroo object")
c=kanga.put_in_pouch(roo)
d=kanga.put_in_pouch("I am a baby Kangaroo")
print(c)
