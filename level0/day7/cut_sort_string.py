def solution(myString):
    answer = myString.split('x')
    while('' in answer):
        if '' in answer:
            answer.remove('')
            continue
    answer.sort()
    return answer
