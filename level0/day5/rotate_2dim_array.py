def solution(board, k):
    answer = 0
    for i, tmp_list in enumerate(board):
        for j, num in enumerate(tmp_list):
            if i+j <= k:
                answer += num
    return answer
