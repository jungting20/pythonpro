aa = "{'level':3,'attr':{'power':120,'name':'hero'}," \
     "'friendIds':[12,23,34,23]}"

#문자열 형식 바꿔주려면 eval 쓰면된다
bb = eval(aa)

#이건 내가한게 더 짧음 ㅋ
def chen(n):
     count = 0
     a = revernum(n)
     print(a)
     r = 0
     while True:
         r = a+n
         count += 1
         if r == revernum(r):
             break
         a,n = r,revernum(r)
     return count,r

def revernum(a):
    c = list(str(a))
    c.reverse()
    return int(''.join(c))


print(chen(195))