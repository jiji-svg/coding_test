def solution(n):
    mod = 1234567
    d = [0]*(n+1)
    d[0] = 0
    d[1] = 1
    for i in range(2, n+1):
        d[i] = (d[i-1] + d[i-2]) % mod
        
    answer = d[-1]
    return answer
