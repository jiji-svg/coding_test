def solution(myString, pat):
    here = 0
    for i, idx in enumerate(myString):
        if myString[i:].startswith(pat):
            here = i
    answer = myString[:here+len(pat)]
    return answer
