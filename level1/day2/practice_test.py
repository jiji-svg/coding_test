def solution(answers):
    answer = {1:0, 2:0, 3:0}
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    max_num = 0
    bests = []
    
    for i, a in enumerate(answers,1):
        a1, a2, a3 = p1[i%5-1], p2[i%8-1], p3[i%10-1]
        if a1 == a:
            answer[1] += 1
        if a2 == a:
            answer[2] += 1
        if a3 == a:
            answer[3] += 1
            

