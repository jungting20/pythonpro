def googoodan(dan,n):
    if n == 1:
        print(str(dan) + 'x' + str(n),dan*n)
        return
    aa =googoodan(dan,n-1)
    print(str(dan) + 'x' + str(n),dan*n)
    return aa

googoodan(9,9)


