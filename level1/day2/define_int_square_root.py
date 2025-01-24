def solution(n):
    if (n%(n**0.5)==0):
        return ((n**0.5)+1)**2
    return -1
