def solution(k, score):
    answer  = []
    tmp_list = []
    
    for s in score:
        if len(tmp_list) < k:
            tmp_list.append(s)
        elif min(tmp_list) < s:
            tmp_list.remove(min(tmp_list))
            tmp_list.append(s)
        answer.append(min(tmp_list))
    return answer
