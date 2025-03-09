from collections import deque
def solution(s):
    par_deq = deque([])
    for i in s:
        par_deq.append(i)
        if len(par_deq) > 1:
            if (par_deq[-2], par_deq[-1]) == ('(', ')'):
                par_deq.pop()
                par_deq.pop()
    if par_deq:
        return False
    else:
        return True
    
