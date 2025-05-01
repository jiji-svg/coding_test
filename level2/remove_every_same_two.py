def solution(s):
    
    s = list(s)
    tmp_s = []
    idxs = set()
    prev_alp = 0
    for i,alp in enumerate(s):
        tmp_s.append(alp)
        if len(tmp_s) == 1:
            pass
        else:
            if tmp_s[-1] == tmp_s[-2]:
                tmp_s.pop()
                tmp_s.pop()
    if tmp_s:
        return 0
    else:
        return 1
    
    

