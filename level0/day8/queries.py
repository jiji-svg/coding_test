def solution(arr, queries):
    answer = arr.copy()
    for query in queries:
        s, e = query
        for i in range(s, e+1):
            answer[i] += 1
    return answer
