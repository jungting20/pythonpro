
def fibo():
    a,b,list = 1,2,[1,2]
    while True:
        list.append(a+b)
        a,b = b,a+b
        if a+b >=  4*(10**6):
            break
    return sum([number for number in list if number % 2 == 0])



print(fibo())


