def solution(new_id):
    answer = ''
    opt = ['-', '_', '.']
    point_add = True
    
    # 1~3 단계
    for alp in new_id:
        if alp.isalpha():
            answer += alp.lower()
            point_add = True
            
        elif alp.isdigit():
            answer += alp
            point_add = True
            
        else:
            if alp in opt:
                if (alp == '.') and (point_add):
                    point_add = False
                    answer += alp
                elif alp != '.':
                    answer += alp
                    point_add = True
    # 4단계
    try:
        while((answer[0]=='.') or answer[-1]=='.'):
            # print(answer)
            if answer[0] == '.':
                answer = answer[1:]
            if answer[-1] == '.':
                answer = answer[:-1]
    except Exception as e:
        pass
    # 5단계
    if not answer:
        answer += 'a'
    
    # 6-1단계, 글자수 15개로 제한
    if len(answer) >= 16:
        answer = answer[:15]
    
    # 6-2 단계, 끝에 . 제거
    while(answer[-1] == '.'):
        answer = answer[:-1]
    
    # 7단계
    while(len(answer) <=2):
        answer = answer + answer[-1]
        
    
                    
                
    return answer

