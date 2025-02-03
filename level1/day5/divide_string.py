def solution(s):
    answer = 0
    count_x = 0
    count_e = 0
    str_all = ''
    for_check = 0
    all_list = []
    
    for x in s:
        if not count_x:
            str_all += x
            a = x
            count_x += 1
            continue
        
        if a == x:
            str_all += x
            count_x += 1
            
        if a != x:
            str_all += x
            count_e += 1
            
        if count_x == count_e:
            for_check += count_x + count_e
            all_list.append(str_all)
            str_all = ''
            count_e=count_x=0
            
    if for_check != len(s):
        diff = len(s) - for_check
        all_list.append(s[:diff:-1])
    answer = len(all_list)
    return answer
