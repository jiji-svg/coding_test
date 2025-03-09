def solution(n):
    answer = ''
    list_124 = ['4', '1', '2']
    
    while(n>0):
        
        idx = n%3
        # 한자리수면 바로 하고 그 다음거부터는 3의 배수이면 1을 빼줘야해서 이순서로.
        if n%3==0:
            n -= 1
        n //= 3
        
        answer += list_124[idx]
    answer = answer[::-1]
    
    return answer
