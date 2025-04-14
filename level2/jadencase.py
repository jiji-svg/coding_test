def solution(s):
    answer = ''
    for idx, alpha in enumerate(s):
        if ((idx == 0) or (s[idx-1] == ' ')) and (alpha.isalpha()):
            answer += alpha.upper()
        else:
            answer += alpha.lower()
    return answer
