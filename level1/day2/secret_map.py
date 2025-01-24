def solution(n, arr1, arr2):
    answer = []
    for num1, num2 in zip(arr1, arr2):
        num1_2 = bin(num1)[2:].zfill(n)
        num2_2 = bin(num2)[2:].zfill(n)
        
        # print(num1_2)
        # print(num2_2)
        sum_2 = ''
        for str1, str2 in zip(num1_2, num2_2):
            if (str1=='1' or str2=='1'):
                sum_2 += '#'
            else:
                sum_2 += ' '
        # print(sum_2)
        answer.append(sum_2)
    return answer
