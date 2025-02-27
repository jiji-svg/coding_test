def solution(friends, gifts):
    answer = 0
    friend_num = len(friends)
    friend_list = [[0 for _ in range(friend_num)] for _ in range(friend_num)]
    friend_num_dict = {} # friend 들의 위치값 저장
    friend_gift_dict = {} # 선물 지수 저장
    friend_set = set()
    for i in range(friend_num-1):
        for j in range(i+1, friend_num):
            friend_set.add((friends[i], friends[j]))
            
    
    for i, me in enumerate(friends):
        friend_num_dict[me] = i
        friend_gift_dict[me] = 0
    
    for gift in gifts:
        give, given = gift.split()
        give_idx, given_idx = friend_num_dict[give], friend_num_dict[given]
        friend_list[give_idx][given_idx] += 1
        friend_gift_dict[give] += 1
        friend_gift_dict[given] -= 1
    
    for friend_partner in friend_set:
        p1, p2 = friend_partner
        p1_idx, p2_idx = friend_num_dict[p1], friend_num_dict[p2]
        if friend_list[p1_idx][p2_idx] > friend_list[p2_idx][p1_idx]:
            friend_list[p1_idx][p1_idx] += 1
        elif friend_list[p2_idx][p1_idx] > friend_list[p1_idx][p2_idx]:
            friend_list[p2_idx][p2_idx] += 1
        else:
            if friend_gift_dict[p1] > friend_gift_dict[p2]:
                friend_list[p1_idx][p1_idx] += 1
            elif friend_gift_dict[p2] > friend_gift_dict[p1]:
                friend_list[p2_idx][p2_idx] += 1
            else:
                pass
        
    all_result = []
    for i in range(friend_num):
        all_result.append(friend_list[i][i])
    answer = max(all_result)
    
        
        
        
    return answer
