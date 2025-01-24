def solution(sizes):
    answer = 0
    width = 0 # 가로
    length = 0 # 세로
    
    for size in sizes:
        w, l = size
        if w<l:
            w,l=l,w
        
        if w>width:
            width=w
        if l>length:
            length=l
    answer = width*length
    return answer
