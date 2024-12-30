def solution(n, control):
    answer = n
    for i, alp in enumerate(control):
        joy_dict = dict(zip(['w', 's', 'd', 'a'], [1, -1, 10, -10]))
        answer += joy_dict[alp]
    return answer

