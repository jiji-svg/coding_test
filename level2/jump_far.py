def solution(n):
    # 점화식
    # d[n] = d[n-2] + d[n-1]
    # d[0] = 1, d[1] = 1
    
    d = [0]*(n+1)
    d[0] = 1
    d[1] = 1
    mod = 1234567
    for i in range(2, n+1):
        d[i] = (d[i-1] + d[i-2]) % mod
    
    answer = d[-1]
    return answer
