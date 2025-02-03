def solution(s, skip, index):
    answer = ''
    alps = 'abcdefghijklmnopqrstuvwxyz'

    for a in skip:
        alps = alps.replace(a, '')
    for a in s:
        answer += alps[(alps.index(a) + index)%(26-len(skip))]
    return answer
