def solution(park, routes):
    answer = []
    for i, p in enumerate(park):
        if 'S' in p:
            sx = i
            sy = p.index('S')
    start = (sy, sx)
    
    
    r_dict = {'E': (1,0), 'W': (-1,0), 'N':(0,-1), 'S':(0,1)}
    
    for route in routes:
        direct, times = route.split()
        times = int(times)
        x, y = r_dict[direct]
        tmp_loc = start
        
        new_x = start[0] + x*times
        new_y = start[1] + y*times

        if (new_x < 0) or (new_x > len(park[0])-1) or (new_y <0) or (new_y > len(park)-1):
            new_x, new_y = start
            
            continue

        # 여기
        for _ in range(times):
            tmp_loc = (tmp_loc[0]+x, tmp_loc[1]+y)
            park_loc = park[tmp_loc[1]][tmp_loc[0]]
            if park_loc == 'X':
                x=0
                y=0
                break

