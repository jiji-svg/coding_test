def solution(arr, queries):
    answer = []
    for query in queries:
        s, e, k = query
        anss = []
        for i in range(s, e+1):
            if (arr[i] > k):
                anss.append(arr[i])
        if anss:
            answer.append(min(anss))
        else:
            answer.append(-1)
        
    return answer
