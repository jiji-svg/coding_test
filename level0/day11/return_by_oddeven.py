def solution(n):
    if n%2==1:
        return sum(num for num in range(1, n+1,2))
    else:
        return sum(num**2 for num in range(0, n+1,2))
