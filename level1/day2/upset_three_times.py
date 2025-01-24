def solution(n):
    def to_three(n):
        third = ''
        while (n > 0):
            third += str(n % 3)
            n //= 3
        return third
    three = to_three(n)
    answer = int(three, 3)
    
    return answer
