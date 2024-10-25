def solution(quiz):
    quizs = quiz.copy()
    
    answer = []
    for sen in quizs:
        
        quiz_list = sen.split(' ')
        if quiz_list[1] == '+':
            if int(quiz_list[0]) + int(quiz_list[2]) == int(quiz_list[4]):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if int(quiz_list[0]) - int(quiz_list[2]) == int(quiz_list[4]):
                answer.append("O")
            else:
                answer.append("X")
        
            
    return answer
