import re
count = 0
#내가푼답
for i in range(1,10001):
    aa = re.findall(r'[8]',str(i))
    if aa:
        count += len(aa)

print(count)

#문자열 리스트에서 카운트 셀수 있다!
#그냥 리스트 자체가 문자열로 됨 그니까 [,8,8,8,이게다 문자열 [도 문자열!!
print(str(list(range(1,10001))).count('8'))


