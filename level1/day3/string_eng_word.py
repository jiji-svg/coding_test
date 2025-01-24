def solution(s):
    answer = 0
    nums = ['0','1','2','3','4','5','6','7','8','9']
    str_nums = ['zero', 'one','two','three','four','five','six','seven','eight','nine']
    for i_n, s_n in zip(nums, str_nums):
        s = s.replace(s_n, i_n)
    answer = int(s)
    
    return answer
