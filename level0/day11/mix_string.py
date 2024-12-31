def solution(str1, str2):
    answer = ''.join(map(lambda x: x[0]+x[1],zip(str1,str2)))
    return answer
