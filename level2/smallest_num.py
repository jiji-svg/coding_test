def solution(A,B):
    
    f_sum = 0
    A.sort()
    B.sort(reverse = True)
    
    for a, b in zip(A,B):
        f_sum += a*b
        

    return f_sum
