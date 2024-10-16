def solution(i, j, k):
    answer = 0
    for num in range(i, j+1):
        str1 = str(num)
        str2 = str(k)
        counts = str1.count(str2)
        answer += counts
    return answer

