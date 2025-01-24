def solution(lottos, win_nums):
    ranks = [6,6,5,4,3,2,1]
    
    cnt_0 = lottos.count(0)
    cnt_same = 0
    
    for my_num in lottos:
        if my_num in win_nums:
            cnt_same += 1
            
    answer = [ranks[cnt_0+cnt_same], ranks[cnt_same]]
        
        
    return answer
