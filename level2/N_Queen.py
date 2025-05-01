def solution(n):
    result = 0
    board = [0]*n
    
    def is_on_ok(current_row):
        for prev_row in range(current_row):
            if board[prev_row] == board[current_row] or \
            abs(board[prev_row]-board[current_row]) == current_row - prev_row:
                return False
        return True
    
    def dfs(row):
        nonlocal result
        if row == n:
            result += 1
            return
        for col in range(n):
            board[row] = col
            if is_on_ok(row):
                dfs(row+1)
    dfs(0)
    return result
