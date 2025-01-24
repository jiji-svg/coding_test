def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    lost2 = lost.copy()
    reserve2 = reserve.copy()
    answer = n - len(lost)
    for l in lost:
        if l in reserve:
            reserve2.remove(l)
            lost2.remove(l)
            answer += 1
    for l in lost2:
        if l-1 in reserve2:
            reserve2.remove(l-1)
            answer += 1
        elif l+1 in reserve2:
            reserve2.remove(l+1)
            answer += 1
    return answer
