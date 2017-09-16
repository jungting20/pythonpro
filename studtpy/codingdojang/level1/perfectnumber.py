from collections import defaultdict

d =defaultdict(int)
for n in range(1,1001):
    for x in str(n):
        d[x] +=1

print(d)


#아 맵 쓸때 저 앞에 있는 저거는 함수임 하나하나 뽑고 그 함수 실행해서 리스트로
#뽑아줌
#람다 쓸수있다
print(''.join(map(str,range(1,1001))))

#eval은 문자열을 그냥 파이선 코드처럼 쓰는거임
print(sum([eval('*'.join(str(x))) for x in range(10,1001)]))




