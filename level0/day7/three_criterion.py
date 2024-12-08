def solution(myStr):
    criterion = ['a', 'b', 'c']
    string = ''
    answer = []
    
    for alpha in myStr:
        if (string == '') and (alpha in criterion):
            continue
        if alpha not in criterion:
            string += alpha
            
        else:
            answer.append(string)
            string = ''
    answer.append(string)
        
    if answer == ['']:
        answer = ['EMPTY']
    return answer
