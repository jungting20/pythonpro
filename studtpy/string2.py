n = 42
f = 7.03
s = 'string cheese'

aa = {'n':42,'f':7.03,'s':'string cheese'}
bb = {'n':40,'f':6.03,'s':'cheese'}
#이걸 기억하자 깔끔하게 기억 넣는순서가있음 딕셔너리는 객체니까 그냥 1개로 보는
#거임 그러니
#결국 저 숫자 0 1의 의미는 .format에 인자에 넣는 순서를 말하는거임 ㅋ
#깨달았다
bb = '{0[n]:<10d} {0[f]:<10f} {0[s]:<10s} {1[n]} {1[f]} {1[s]}'.format(aa,bb)
cc = '{0:0>2d}'.format(1)
print(cc)

