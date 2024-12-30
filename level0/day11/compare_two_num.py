def solution(a, b):
    aa=[a,b]
    return max((2*a*b), int(''.join(map(str,aa))))
