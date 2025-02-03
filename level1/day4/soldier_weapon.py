def solution(number, limit, power):
    def get_divisor(num):
        divs = []
        for i in range(1, int((num**0.5))+1):
            if num%i == 0:
                divs.append(i)

        new_divs = []
        for n in divs:
            new_divs.append(num//n)
        final_divs = list(set(divs + new_divs))
        count = len(final_divs)
        if count > limit:
            count = power
        return count
    tmp = [get_divisor(x) for x in range(1, number+1)]
    
    
    answer = sum(tmp)
    
    return answer
