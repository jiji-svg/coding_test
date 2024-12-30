def solution(numLog):
    answer = ''
    nums = [1, -1, 10, -10]
    alps = ['w', 's', 'd', 'a']
    for i, num in enumerate(numLog):
        if i == 0:
            first = num
        else:
            idx = num - first
            first = num
            answer += alps[nums.index(idx)]
    # nums = [1, -1, 10, -10]
    return answer
