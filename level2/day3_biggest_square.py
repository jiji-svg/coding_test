def solution(board):
    x_m, y_m = len(board), len(board[0])
    max_len = 0
    for x in range(x_m):
        for y in range(y_m):
            if board[x][y] == 1:
                if x==0 or y==0:
                    max_len = max(max_len, 1)
                else:
                    board[x][y] = min(board[x-1][y], board[x-1][y-1],board[x][y-1]) + 1
                    max_len = max(max_len, board[x][y])
    return max_len**2


