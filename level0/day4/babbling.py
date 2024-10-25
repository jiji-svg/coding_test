def solution(babbling):
    can_do = ['aya', 'ye', 'woo', 'ma']
    answer = 0
    for bab in babbling:
        total_len = len(bab)
        for can in can_do:
            cnt = bab.count(can)
            if cnt:
                total_len -= cnt * len(can)
            
        if not total_len:
            answer += 1
    


