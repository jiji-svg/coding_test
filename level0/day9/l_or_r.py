def solution(str_list):
    answer = []
    for i, st in enumerate(str_list):
        if st == 'l':
            answer = str_list[:i]
            break
        elif st == 'r':
            answer = str_list[i+1:]
            break
    return answer


