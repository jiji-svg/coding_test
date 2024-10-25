def solution(my_string):
    def calculate(num1, num2, op):
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
    my_string = my_string.split()
    num_sum = int(my_string[0])
    for i in range(2, len(my_string)+1, 2):
        num_sum = calculate(num_sum, int(my_string[i]), my_string[i-1])
    answer = num_sum


    return answer
