def solution(num, total):
    if num == 1:
        return [total]
    s0 = 0
    answer = []
    for i in range(-51, total):
        s0 = 0
        for j in range(num):
            s0 += i+j
        if s0 == total:
            for k in range(num):
                answer.append(k+i)
            return answer
#     if num == 1:
#         return [total]
#     answer = []
#     tmp_total = 0
#     for j in range(num):
#         tmp_total += j
#     for i in range((-total), total+1):
        
#         if (num*i + tmp_total) == total:
#             for j in range(num):
#                 answer.append(i+j)
#             return answer

