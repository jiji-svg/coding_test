def solution(left, right):
    answer = 0
    def get_yak(num):
        count = 0
        for n in range(1, num+1):
            if num%n == 0:
                count += 1
        if count%2==0:
            return num
        else:
            return -num
    for n in range(left, right+1):
        answer += get_yak(n)
    return answer
