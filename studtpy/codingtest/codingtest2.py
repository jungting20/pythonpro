mesg = "SMS"


def solution(S,K):
    if len(S) < K:
        return -1
    length = len(S)
    return length//K if length%K==0 else length//K+1

print(solution(mesg,12))