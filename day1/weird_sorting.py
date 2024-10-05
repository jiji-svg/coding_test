def solution(numlist, n):
    num_dict = {}
    for num in numlist:
        num_dict[num] = abs(num-n)
    tmp_list = []    
    for key, value in num_dict.items():
        tmp_list.append([value, key])
        
    tmp_list.sort(key=lambda x: (x[0], -x[1]))
    
    answer = []
    for nums in tmp_list:
        answer.append(nums[1])
    return answer

