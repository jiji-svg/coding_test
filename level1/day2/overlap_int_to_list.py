def solution(n):
    n = str(n)
    answer = [int(n[i]) for i in range(len(n)-1,-1,-1)]
    # answer = list(map(int, reversed(str(n))))
    return answer
