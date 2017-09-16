#내가한거
def addunder_bar(stri):
     import re
     list_st = list(stri)
     n = 0
     for i in re.findall('[A-Z0-9]',stri):
         list_st.insert(stri.index(i)+n,'_')
         n += 1
     print(''.join(list_st).lower())
string = 'codingDojang'
addunder_bar(string)
#남이한거 중 베스트삘
#A if condition else B 는 파이썬 3항연산자!!!
#조건 만족하면 A 아니면 B 이거 인듯


def do(l):
    a="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(['_'+c.lower if c in a else c for c in l])
