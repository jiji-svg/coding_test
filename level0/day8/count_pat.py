def solution(myString, pat):
    # answer = myString.count(pat)
    answer = 0
    total_len = len(myString)
    test_len = len(pat)
    for idx in range(0, total_len-test_len+1):
        if myString[idx:idx+test_len] == pat:
            answer += 1
    return answer
