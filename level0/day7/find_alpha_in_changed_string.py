def solution(myString, pat):
    answer = ''
    for alp in myString:
        if alp == 'A':
            answer += 'B'
        else:
            answer += 'A'
    if pat in answer:
        return 1
    else:
        return 0
