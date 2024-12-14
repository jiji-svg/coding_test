def solution(arr, query):
    answer = arr
    for i, num in enumerate(query):
        if i%2==0:
            answer = answer[:num+1]
        else:
            answer = answer[num:]
    return answer
