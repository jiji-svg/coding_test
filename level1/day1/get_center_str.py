def solution(s):
    center = len(s)//2
    total_length = len(s)
    answer =  s[center] if total_length%2==1 else s[center-1:center+1]
    return answer
