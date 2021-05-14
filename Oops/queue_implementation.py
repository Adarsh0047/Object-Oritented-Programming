import queue
n=eval(input("Enter Max Size of queue: "))
x=queue.Queue(maxsize=n)
print(x.qsize())

for i in range(n):
    print("Input ", i+1, "element: ")
    a=input()
    x.put(a)
for i in range(n):
    print(i+1,"element: ")
    print(x.get())

