
def solution(code):
    return "".join(code.split("1"))[::2] or "EMPTY"
#     answer = ''
#     mode = 0
#     for idx, a in enumerate(code):
        
#         if mode == 0:
#             if a == '1':
#                 mode = 1
#             elif idx%2==0:
#                 answer+=a
#         else:
#             if a == '1':
#                 mode = 0
#             elif idx%2==1:
#                 answer+=a
#     if not answer:
#         return "EMPTY"
    return answer
