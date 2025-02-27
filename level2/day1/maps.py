from collections import deque
def solution(maps):
    answer = -1
    d1 = deque([(0,0,1)])
    moves = [(1,0), (-1,0), (0,1), (0,-1)]
    x_m, y_m = len(maps), len(maps[0])
    visited = set()
    
    
    while(d1):
        x, y, cnt = d1.popleft()
        
        for dx, dy in moves:
            nx, ny = x+dx, y+dy

            if (nx, ny) == (x_m-1, y_m-1):
                return cnt+1

            if (0<=nx<x_m) and (0<=ny<y_m) and ((nx, ny) not in visited) and (maps[nx][ny]==1):
                visited.add((nx,ny))
                d1.append((nx,ny,cnt+1))
    
    
    return answer
