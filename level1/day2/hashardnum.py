def solution(x):
    str_x = sum(int(a) for a in str(x))
    answer = not bool(x%str_x)
    return answer
