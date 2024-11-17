def solution(a, b):
    if ((a+b)%2 == 0):
        if a % 2 == 1:
            answer = a**2 + b**2
        else:
            answer = abs(a-b)
    else:
        answer = 2 * (a+b)
    return answer
