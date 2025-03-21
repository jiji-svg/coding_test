def max_divisor(num):
    ans = [1]
    if num == 1:
        return 0
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0 and i!= num:
            ans.append(i)
            if num//i <= 1e7 and num//i != num:
                ans.append((num // i))
    return max(ans)

def solution(begin, end):
    answer = []
    for i in range(begin, end+1):
        answer.append(max_divisor(i))
    return answer
