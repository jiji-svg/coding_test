def solution(k, m, score):
#     answer = 0
#     apples = sorted(list(set(score)),reverse=True)
#     apple_dict = {}
#     for apple in apples:
#         apple_dict[apple] = score.count(apple)
    
#     remain = 0
#     for apple in apples:
#         answer += ((apple_dict[apple]+remain) // m) * apple * m
        
#         remain += apple_dict[apple] % m
#         remain = remain % m        
    # return answer
    return sum(sorted(score)[len(score)%m::m])*m
