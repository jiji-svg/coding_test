def solution(ineq, eq, n, m):
    try:
        answer = int(eval((ineq+eq).join([str(n),str(m)])))
    except:
        answer = int(eval((ineq).join([str(n),str(m)])))
    
    return answer
