

class Element:
    def __init__(self,name,symbol,number):
        self.__name=name
        self.__symbol=symbol
        self.__number=number

    def dump(self):
        print('name=%s,symbol=%s,number=%s' % (self.name,self.symbol,self.number))

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number

aa=Element('Hydrogen','H',1)
print(aa.name)


