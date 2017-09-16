class Element():
    def __init__(self,name,symbol,number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name

    def dump(self):
        return self.name+self.symbol+self.number

    def __str__(self) -> str:
        return self.name+self.symbol+str(self.number)


aa = {'name':'Hydrogen','symbol':'H','number':1}

bb = Element(**aa)

print(bb.name)

