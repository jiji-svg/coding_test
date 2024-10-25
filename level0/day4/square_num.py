def solution(n):
    for i in range(1, n//2):
        if i*i == n:
            answer = 1
            break
        else:
            answer = 2
    return answer

