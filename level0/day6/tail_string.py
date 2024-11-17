def solution(str_list, ex):
    return ''.join(filter(lambda x:ex not in x, str_list))
#     answer = ''
#     for sen in str_list:
#         if ex not in sen:
#             answer += sen
    
#     return answer
