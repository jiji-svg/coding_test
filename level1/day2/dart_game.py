def solution(dartResult):
    answer = 0
    bonus = ['S', 'D', 'T']
    opt = ['*', '#']
    # only_nums = []
    nums = {0:0, 1:0, 2:0}
    num_idx = 0
    res = 0
    dartResult_num = ''
    dartResult_str = ''
    
    for alp in dartResult:
        if (alp in bonus) or (alp in opt):
            dartResult_num += ' '
            dartResult_str += alp
        else:

