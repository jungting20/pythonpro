import re


#이건 보니까 파이썬 스킬임
#매칭되는 글자 찾아서 다 바꾸는 법
aa = re.sub(r'([13579]{2})|([02468]{2})',
            lambda match:  '-'.join(match.group(1))
            #'-'.join('44')이거임 결국
            if match.group(1) else '*'.join(match.group(2)), '445566')
print(aa)


bb = re.finditer(r'([13579]{2})|([02468]{2})','445566')




