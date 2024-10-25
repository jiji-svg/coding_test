def solution(array):
    max_num = max(array)
    idx = array.index(max_num)
    answer = [max_num, idx]
    return answer

