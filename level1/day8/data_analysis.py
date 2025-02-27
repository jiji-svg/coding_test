def solution(data, ext, val_ext, sort_by):
    code_num = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
    answer = [x for x in data if x[code_num[ext]] <= val_ext]
    answer = sorted(answer, key=lambda x:x[code_num[sort_by]])
    
    return answer
