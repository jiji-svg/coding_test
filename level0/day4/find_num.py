def solution(num, k):
    # str_num = str(num)
    # if str(k) in str_num:
    #     answer = int(str_num.index(str(k))) + 1
    # else:
    #     answer = -1
    try:
        answer = str(num).index(str(k)) + 1
    except:
        answer = -1
    return answer
