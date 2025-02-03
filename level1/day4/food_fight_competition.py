def solution(food):
    answer = ''
    food_dict = {}
    for i,f in enumerate(food):
        if i == 0:
            continue
        food_dict[str(i)] = f // 2
    
    string1 = []
    
    for key, value in food_dict.items():
        string1.append((key,value))
        answer += key * value
    answer += '0'
    
    for i in range(len(string1)):
        string = string1.pop()
        j, k = string
        answer += j * k
        
        
    return answer
