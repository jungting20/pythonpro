aa = '4546793'
bb = ''
#내가푼답
for i in range(0,len(aa)):
    if i == len(aa)-1:
        bb +=aa[len(aa)-1]
        break
    if int(aa[i]) % 2 == 0:
        if int(aa[i+1]) % 2 == 0:
            bb += aa[i]+'*'
        else:
            bb += aa[i]
    else:
        if int(aa[i+1])%2 != 0:
            bb+=aa[i]+'-'
        else:
            bb+=aa[i]

print(bb)

