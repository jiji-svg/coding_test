def solution(a, d, included):
    answer = 0
    nums = [a+d*i for i in range(len(included))]
    tmp_ans = list(map(lambda x: x[0]*x[1], zip(nums, included)))
    answer = sum(tmp_ans)
    # print(list(zip(nums,included)))
    return answer
