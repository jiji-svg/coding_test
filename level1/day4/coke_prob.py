def solution(a, b, n):
    answer = 0
    while(1):
        remain = n % a
        n = n // a * b
        answer += n
        
        if n == 0:
            break
            
        else:
            n = n + remain
    
    return answer
