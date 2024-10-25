from collections import deque
def solution(A, B):
    if A == B:
        return 0
    answer = 0
    while(answer < len(A)):
        answer += 1
        A = A[-1] + A[0:-1]
        if A == B:
            return answer
    answer = -1
    
    #1 answer = (B*2).find(A)
    
    #2 a, b = deque(A), deque(B)
    # for cnt in range(0, len(A)):
    #     if a == b:
    #         return cnt
    #     a.rotate(1)
    # return -1
    return answer

