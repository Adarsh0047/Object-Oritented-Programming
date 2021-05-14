Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> b="55"
>>> b.split()
['55']
>>> b
'55'
>>> li=[]
>>> for i in b:
	li.append(i)

	
>>> print(li)
['5', '5']
>>> for j in li:
	add=add+int(j)

	
Traceback (most recent call last):
  File "<pyshell#12>", line 2, in <module>
    add=add+int(j)
NameError: name 'add' is not defined
>>> add=0
>>> for j in li:
	add=add+int(j)

	
>>> print(add)
10
>>> 
