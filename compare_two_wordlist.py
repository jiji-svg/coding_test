def solution(before, after):
    def make_dict(list1):
        tmp_dict = {}
        for i in list1:
            if i in tmp_dict:
                tmp_dict[i] += 1
            else:
                tmp_dict[i] = 1
        return tmp_dict
    dict_before, dict_after = make_dict(before), make_dict(after)
    
    if dict_before == dict_after:
        return 1
    else:
        return 0

