
def njinsoo(base,number):
    T='0123456789ABCDEF'
    m,n = divmod(number,base)
    if m==0:
        return T[n]
    else:
        print(base,m,n,T[n])
        return njinsoo(base,m)+T[n]

print(njinsoo(8,233))


