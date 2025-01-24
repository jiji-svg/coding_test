import math
def solution(n, m):
    # answer = [math.gcd(n,m),(n*m)//math.gcd(n,m)]
    def gcd(n,m):
        tmp_ans = 1
        i = 2
        while((i <= m) or (i <= n)):
            
            if (m%i==0) and (n%i==0):
                tmp_ans *= i
                m //= i
                n //= i
                i = 2
                continue
            i += 1
        return tmp_ans
    
    gcd_ans = gcd(n,m)
    lcm_ans = (m*n) // gcd_ans
        
    answer = [gcd_ans, lcm_ans]
    return answer
