def solution(numbers):
    answer = []
    for i, num in enumerate(numbers):
        
        for j in range(len(numbers)-i-1):
            answer.append(num+numbers[j+i+1])
    print(answer)
    answer = list(set(answer))
    answer.sort()
        
    return answer
