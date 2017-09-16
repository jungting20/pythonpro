import string,re
printable = string.printable
m = re.findall('\s',printable)
print(m)
#I다음 am
' (?<=I) am'
#wish 이전 i
'i (?=wish)'