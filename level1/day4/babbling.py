def solution(babbling):
    answer = 0
    can_dos = ['aya', 'ye', 'woo', 'ma']
    
    
    for bab in  babbling:
        for can in can_dos:
            if can*2 in bab:
                continue
            if can in bab:
                while(can in bab):
                    bab = bab.replace(can, ' ')
                # print(bab)
        bab = bab.strip()
        if not bab:
            answer += 1
            
    
    return answer
