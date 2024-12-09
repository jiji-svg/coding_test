def solution(strArr):
    answer = [string for string in strArr if 'ad' not in string]
    # for string in strArr:
    #     if 'ad' not in string:
    #         answer.append(string)
    return answer
