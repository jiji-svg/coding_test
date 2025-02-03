def solution(cards1, cards2, goal):
    a = []
    answer = ''
    
    for i, word in enumerate(goal):
        
        if cards1 != []:
            if cards1[0] == word:
                a.append(cards1.pop(0))
                continue
                
        if cards2 != []:
            if cards2[0] == word:
                a.append(cards2.pop(0))
                continue
        return 'No'   
        
    return 'Yes'
