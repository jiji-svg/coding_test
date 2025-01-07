def solution(s):
    flag = ((len(s)==4) or (len(s)==6)) and (s.isnumeric())
    if flag:
        return True
    return False
