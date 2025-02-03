def solution(s):
    answer = []
    for i, a in enumerate(s):
        if i == 0:
            answer.append(-1)
            continue
        idx = s[i-1::-1].find(a)
        if idx != -1:
            idx = idx +1
        answer.append(idx)
    
    
    return answer
