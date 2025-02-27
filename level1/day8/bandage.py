def solution(bandage, health, attacks):
    hp = health
    answer = 0
    t_count = 0
    t_max, heal, more_heal = bandage
    last_attack_time = attacks[-1][0]
    attacks_dict = {}
    for attack in attacks:
        time, damamge = attack
        attacks_dict[time] = damamge
    
    for i in range(1, last_attack_time+1):
        
        if i in attacks_dict:
            hp -= attacks_dict[i]
            t_count = 0
        else:
            t_count += 1
            hp += heal
        
        if t_count == t_max:
            t_count = 0
            hp += more_heal
        
        if hp > health:
            hp = health
        if hp <= 0:
            return -1
        
    return hp

