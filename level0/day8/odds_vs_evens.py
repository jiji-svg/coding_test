def solution(num_list):
    odds = sum(num_list[::2])
    evens = sum(num_list[1::2])
    return max(odds, evens)
    # flags = [False if i%2==0 else True for i in range(len(num_list))]
    # odds = 0
    # evens = 0
    # for flag, num in zip(flags, num_list):
    #     if flag:
    #         odds += num
    #     else:
    #         evens += num
    # if odds > evens:
    #     return odds
    # else:
    #     return evens
