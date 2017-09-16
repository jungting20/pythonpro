import random


arr=[]
arr2=[0]*21

for i in range(1,21):
    arr.append(random.randint(1,20))

for i in range(0,len(arr)-1):
    arr2[arr[i]]=arr2[arr[i]]+1;



number = -1
strarr = []
for i in arr2:
    number += 1
    if i % 2 != 0:
        str = bin(number)
        strarr.append(str[2:])
print(strarr)

idx = -1
result = ""
for i in strarr:
    young = 0
    il = 0
    for j in len(i):
        idx += 1
        if i[::-1][idx] == '0':
            young += 1
        else:
            il += 1
    if young % 2 != 0:
        young = 1
    else:
        young = 0
    if il % 2 != 0:
        il = 1
    else:
        il = 0

    if young != il:
        result += '1'

print(result)