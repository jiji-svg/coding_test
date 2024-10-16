def solution(score):
    avg_score = [(k[0]+k[1])/2 for k in score]
    print(avg_score)
    def ranking(num, list0):
        rank = 1
        for avg in list0:
            if num < avg:
                rank += 1
                
        return rank
    answer = []
    for num in avg_score:
        rank = ranking(num, avg_score)
        answer.append(rank)
    return answer
