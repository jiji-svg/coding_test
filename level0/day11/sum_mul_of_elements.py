def solution(num_list):
    num_mul = eval('*'.join(str(n) for n in num_list))
    square_sum = sum(num_list) ** 2
    return 1 if num_mul < square_sum else 0
