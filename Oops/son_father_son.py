class Son:
    def __init__(self):
        self.__fb_id=""
        self.__instra_id=""
        self.whatsapp_id=""
        self._Rstatus=""

    def _relationship_status(self):
        self._Rstatus="Commited"

class Dad(Son):
    def __init__(self):
        self.Dad_fb_id=""
        self.Dad_instra_id=""
        self.Dad_whatsapp_id=""
    def display(self):
        Son._Rstatus="Single"
        print(self._Rstatus)

class Friend(Son):
    def __init__(self):
        self.__Frd_fb_id=""
        self.__Frd_instra_id=""
        self.Frd_whatsapp_id=""
    def print(self):
        Son._Rstatus="Commited"
        print(Son._Rstatus)

s=Son()
s._relationship_status()
d=Dad()
d.display()
f=Friend()
f.print()
    
