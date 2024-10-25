def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    
    def go_left(row, col, cnt):
        while(1):
            try:
                if answer[row][col] == 0:
                    answer[row][col] = cnt
                    col -= 1
                    cnt += 1
                else:
                    return row-1, col+1, cnt
            except:
                return row-1, col+1, cnt
    
    def go_right(row, col, cnt):
        if row == col == 0:
            answer[row][col] = cnt
            cnt += 1
            col += 1
        while(1):
            try:
                if answer[row][col] == 0:
                    answer[row][col] = cnt
                    cnt += 1
                    col += 1
                else:
                    return row+1, col-1, cnt
            except:
                return row+1, col-1, cnt        
    
    def go_up(row, col, cnt):
        while(1):
            try:
                if answer[row][col] == 0:
                    answer[row][col] = cnt
                    cnt += 1
                    row -= 1
                else:
                    return row+1, col+1, cnt
            except:
                return row+1, col+1, cnt
            
    
    def go_down(row,col, cnt):
        while(1):
            try:
                if answer[row][col] == 0:
                    answer[row][col] = cnt
                    cnt += 1
                    row += 1
                else:
                    return row-1, col-1, cnt
            except:
                return row-1, col-1, cnt
                    
    
    cnt = 1
    row, col = 0, 0
    while(cnt <= (n*n)):
                
        row, col, cnt = go_right(row, col, cnt)
        row, col, cnt = go_down(row, col, cnt)
        row, col, cnt = go_left(row, col, cnt)
        row, col, cnt = go_up(row, col, cnt)
            
    return answer
