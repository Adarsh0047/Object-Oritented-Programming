try:
    usernamer=open('D:\\Workspace\\Python\\Login System\\1234.txt','r')
    self.usercontr=self.user_na_r.read()
    print('The file has been read successfully')
except FileNotFoundError:
    print("There is no such file in the directory")
