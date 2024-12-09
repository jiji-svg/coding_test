def solution(arr):
    answer = []
    for x in arr:
        if (x%2==0) and (x>=50):
            answer.append(x/2)
        elif (x%2==1) and (x<50):
            answer.append(x*2)
        else:
            answer.append(x)
    return answer
