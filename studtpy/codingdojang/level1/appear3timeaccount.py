name_list = ['이유덕','이재영','권종표','이재영','박민호',
        '강상희','이재영','김지완','최승혁'
                          ,'이성연','박영서','박민호','전경헌'
        ,'송정환','김재성','이유덕','전경헌']


first_name = [i[0] for i in name_list]
print('김:{0}명,이:{1}명'.format(first_name.count('김'),first_name.count('이')))

print('이재영{0:02d}'.format(name_list.count('이재영')))

print(set(name_list))

list(set(name_list)).sort()



