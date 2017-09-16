#m//n 은 결국 int(m/n) 과같음
def boardpaging(m,n):
    page_count = m//n if m%n==0 else m//n+1
    return page_count

def boardpaging2(m,n):
    page = m//n
    if page != 0:
        page += 1
    print(page)


s_list = [1,3,4,8,13,17,18]
#내가푼답 이건 리얼 진짜 최소값들은 다 찾는 거고
def aas(a):
    s_list_dict={}
    for i in range(0, len(a)-1):
        aaa = str(a[i + 1]) + '-' + str(a[i])
        s_list_dict[aaa] = a[i + 1] - a[i]

    for name,value in s_list_dict.items():
        if value == min(s_list_dict.values()):
            aa = name.index('-')
            print('({1},{0})'.format(name[0:aa],name[aa+1:]))


#짧은답
#zip는 꼭 개수가 맞지않아도 작은거까지 연결됨!
#정렬때릴때 기준을 함수로 줄수 있다
s = [1,3,4,8,13,17,18]
pairs = list(zip(s[0:],s[1:]))
#리스트를 정렬 할때 리스트 요소 하나 하나를 봐주는 함수가 있으면된다
#얘가 정렬 할 때 요소 하나가 듀플이니 그걸 계산해주는게 필요함
#zip 놀랍다
#이렇게도 되고 내가 정의한 sor을 써도 된다
pairs.sort(key=lambda x:x[1]-x[0])
print(pairs[0])
#더 짧은 답
print(min([i for i in zip(s[0:],s[1:])],key=lambda x:x[1]-x[0]))





