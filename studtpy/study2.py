aa = 'BaekjoonOnlineJudgeasdjlsjklsaklkl'

aa_n = len(aa)
print(aa_n)
for i in range(1,int(aa_n/10)+2):
    if 10*i >= aa_n:
        print(aa[int(i - 1) * 10:aa_n])
    else:
        print(aa[int(i-1)*10:(10*i)+1])
