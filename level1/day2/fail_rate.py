from collections import Counter
def solution(N, stages):
    answer = []
    challengers = Counter(stages)
    clear_dict = {}
    peoples = len(stages)
    
    for stage in range(1, N+1):
        on_stage = 0
        clear_people = 0
        for key, value in challengers.items():
            
            if key >= stage :
                on_stage += value
                if key > stage:
                    clear_people += value
            if on_stage == 0:
                clear_dict[stage] = 0
                continue
            clear_dict[stage] = 1-(clear_people / on_stage)
    print(clear_dict)
# sorted_data_desc = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
    answer = sorted(clear_dict, key=lambda k:clear_dict[k], reverse=True)
    print(answer)
    
    return answer
