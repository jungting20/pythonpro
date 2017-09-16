from itertools import groupby
import re
aa = 'aaabbccddaa'

#와 저 \1의 의미는 정규식 괄호친거 저거를 참조하라는소리 그니까
#a와 a여러개 반복된거 두개세트로 나오라고 함
#파인드올은 아마 그룹으로된거 듀플로뽑아줌!!!!!
filted = re.findall(r'(\w)(\1*)',aa)
print(filted)

#그룹바이 ㅋ ㅋ 어마어마하군 ㅋ
for x ,y in groupby(aa):
    print(''.join(y))


def realdap(string):
    count = 1
    ans = ''
    string = string + '\0'
    for i in range(1,len(string)):
        if string[i-1] == string[i]:
            count += 1
        else:
           ans = string[i-1]+str(count)+realdap(string[i:])
           break

    return ans
