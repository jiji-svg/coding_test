def solution(n):
    answer = 0
    k = n+1
    while(1):
        if str(bin(n)).count('1') == str(bin(k)).count('1'):
               return k
        k += 1
    return answer
