def solution(s, n):
    answer = ''
    s_first = ord('a')
    s_end = ord('z')
    l_first = ord('A')
    l_end = ord('Z')
    for alp in s:
        if not alp.isalpha():
            answer += alp
            continue
        if alp.isupper():
            if (ord(alp) + n) > l_end:
                answer += chr((ord(alp)+n)%l_end + l_first - 1)
            else:
                answer += chr(ord(alp)+n)
                
        else:
            if (ord(alp) + n) > s_end:
                answer += chr((ord(alp)+n)%s_end + s_first - 1)
            else:
                answer += chr(ord(alp)+n)
    return answer
