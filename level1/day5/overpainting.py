def solution(n, m, section):
    answer = 0
#     walls = [True]*(n+1)
#     for s in section:
#         walls[s] = False
    
#     wl = len(walls)
    k = 0
    j = 0
    while((k+j)<len(section)):
        if (section[k+j]-section[j]) >= m:
            answer += 1
            j = k+j
            k = 0
        else:
            k += 1
    
    answer += 1
        
                
    return answer
