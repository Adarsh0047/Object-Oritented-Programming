class SuperString:
    def __init__(self,string):
        self._s=string
class Reverse(SuperString):
    def rev(self):
        rev=self._s[::-1]
        print(rev)
class Palindrome(SuperString):
    def Pal(self):
        lower=self._s.lower()
        rev=lower[::-1]
        if lower==rev:
            print("The string is a Palindrome")
        else:
            print("The string is not a Palindrome")


re=Reverse("Dad")
re.rev()
pa=Palindrome("Dad")
pa.Pal()
