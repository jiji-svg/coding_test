def solution(a, b):
    return max(int(''.join(map(str, [a,b]))), int(''.join(map(str,[b,a]))))
