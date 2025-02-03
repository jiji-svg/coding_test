from collections import Counter
def solution(X, Y):

    answer = ''
    inter = []
    inter_dict = {}
    tmp_list = []
    
    count_x = Counter(X)
    count_y = Counter(Y)
    for x_key, x_val in count_x.items():
        if x_key in count_y.keys():
            y_val = count_y[x_key]
            inter_dict[x_key] = min(x_val, y_val)
    # print(inter_dict)
    if inter_dict == {}:
        answer = '-1'
    elif set(inter_dict.keys()) == set('0'):
        
        answer = '0'
    else:
        tmp_list = []
        for key, val in inter_dict.items():
            tmp_list.append(key*val)
        answer = ''.join(sorted(tmp_list, reverse=True))
    
    return answer


