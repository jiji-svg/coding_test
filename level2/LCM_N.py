def is_prime(n):
    num_array = [1 for _ in range(n+1)]
    prime_set = set()
    for i in range(2, n):
        if num_array[i]:
            j = 2
            prime_set.add(i)
            while i*j <= n:
                num_array[i*j] = 0
                j += 1
    return list(prime_set)
        
    
def solution(arr):
    answer = 1
    primes = is_prime(100)
    
    n = primes.pop(0)
    while(n):
        flags = 0
        for i, num in enumerate(arr):
            if num % n == 0:
                flags += 1
                arr[i] = num//n
        if flags:
            answer *= n
        if flags == 0:
            n = primes.pop()
        if sum(arr) == len(arr):
            break
            
                    
                    
        
    return answer
