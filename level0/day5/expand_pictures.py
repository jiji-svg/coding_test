def solution(picture, k):
    answer = []
    for line in picture:
        tmp_line = ''.join([pix*k for pix in line])
        for _ in range(k):
            answer.append(tmp_line)
        
            
    
    return answer
