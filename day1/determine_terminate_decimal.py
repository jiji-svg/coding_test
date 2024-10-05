def solution(a, b):
    
    def find_divisor(x, tmp_list):
        
        for i in range(2, x+1):
            if x % i == 0:
                tmp_list.append(i)
                find_divisor(x//i, tmp_list)
                break
    a_divisor_list = []
    b_divisor_list = []

    find_divisor(a,a_divisor_list)
    find_divisor(b,b_divisor_list)       

    if a_divisor_list is not []:
        for num in a_divisor_list:
            if num in b_divisor_list:
                b_divisor_list.remove(num)

    for num in b_divisor_list:
        if num in [2, 5]:
            answer = 1
        else:
            answer = 2
            break
    if a%b == 0:
        answer = 1
        
    return answer

