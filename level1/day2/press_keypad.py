def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12
    lefts = [1,4,7]
    rights = [3,6,9]
    distance = {1:1, 4:2, 7:3, 10:4, 0:0, 3:1, 6:2, 9:3, 5:3, 2:2, 8:4}
    
    
    
    for i, num in enumerate(numbers):
        
        # 0번 키패트를 11로 취급 (*은 10, #은 12)
        if num == 0:
            numbers[i] = 11
            num = 11
            
        # 1,4,7일때 왼손으로
        if num in lefts:
            
            left = num
            answer += 'L'
            
            continue
        
        # 3,6,9일때 오른손으로
        elif num in rights:
            
            right = num
            answer += 'R'
            

