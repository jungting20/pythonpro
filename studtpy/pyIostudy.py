import re
poem = ''
fin = open('iotest.py','rt')
a = ''.join([line for line in fin])
fin.close()

fin3 = open('iotest.py','rt')
dd = ''.join(fin3.readlines())
print('디디',dd)
fin3.close()

fin4 = open('iotest.py','rt')
for line in fin4.readlines():
    #i 이전에나오는 숫자를 찾자
    #이후는 (?<=i)\d 하면 될듯
    aa = re.findall('\d(?=i)',line)
    #이건 보니까 리스트로 나오네
    if aa:
        print(aa)

fin4.close()



fin2 = open('iotest.py','rt')
poem = ''
while True:
    aa = fin2.readline()
    poem += aa
    if not aa:
        break
fin2.close()

