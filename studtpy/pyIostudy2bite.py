fin = open('20170626_161748.png','rb')
aa = fin.read()
#궁금해서 절반만큼만 읽어봤는데 파일 열어보면 아무것도 안나옴
#그러니 그냥 다 읽어야 할 듯 ㅋ
# aa = fin.read(5000)
print(len(aa))
fin.close()


fin2 = open('aaa.png','wb')
fin2.write(aa)
fin2.close()

#어디에써야할지 모르겠음
#몇바이트까지 이동하는지 그거인듯 ㅅㅂ
fin3 = open('20170626_161748.png','rb')
#마지막 1바이트를 읽으려고 이 짓함
fin3.seek(-1,2)
bb =fin3.read()

fin4 = open('bbb.png','wb')
fin4.write(bb)
fin4.close()
