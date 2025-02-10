def solution(name, yearning, photo):
    answer = []
    ny_dict = {}
    for n, y in zip(name, yearning):
        ny_dict[n] = y
    
    for p in photo:
        tmp_sum = 0
        for person in p:
            if person in name:
                tmp_sum += ny_dict[person]
        answer.append(tmp_sum)
    return answer
