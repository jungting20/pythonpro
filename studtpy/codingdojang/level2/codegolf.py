import functools


list_number = [3,30,39,5,9,881]

#맵을 활용하자 ㅋ 저러면 그냥 하나하나에 다 스트링 끼워짐
list_number = list(map(str,list_number))
#문자열이니까 두개씩묶어서 숫자로바꿔서 그거 비교해서 뽑는듯
#'3'+'30' 과 '30'+'3'을 숫자로 바꾼다음 그걸 비교해서 소트때림 ㅋ
#그니까 cmp_to_key는 리스트내에 값들끼리 조합해서 소트하는방법을 쓸때
#사용하는듯 하다
#모르겠으면 def로 함수만들어서 프린트로 찍어보면댐
list_number.sort(key=functools.cmp_to_key(lambda x,y:int(x+y)-int(y+x)),reverse=True)

print(list_number)


def aaa(x,y):
    print('3엑스란 무엇인가',x,y)
    return 3*x-2*y

las = [1,6,7,8,5,3]
las.sort(key=functools.cmp_to_key(aaa))
print(las)



aa='123'
#True는 1이고 False는 0이니까
print(aa[True]) #2
print(aa[False])#1



