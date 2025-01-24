def solution(board, moves):
    answer = 0
    N = len(board[0])
    basket = []
    for move in moves:
        for i in range(N):
            doll = board[i][move-1]
            if doll == 0:
                continue
            basket.append(doll)
            board[i][move-1] = 0
            break
        if len(basket) > 1:
            if basket[-1] == basket[-2]:
                basket.pop()
                basket.pop()
                answer += 2
    return answer
