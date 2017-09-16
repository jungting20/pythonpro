
#조합 알고리즘
def combination(string,k=0):
    if k == (len(string)-1):
        print(string[len(string)-1])
        return
    list_string = list()
    for i in range(k,len(string)):
        list_string.append(string[i])
        print(''.join(list_string))
    combination(string,k+1)



string = '1234'

combination(string)










