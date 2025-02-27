def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    def str_time_to_second(time):
        mm, ss = time.split(':')
        return int(mm)*60 + int(ss)
    
    pos = str_time_to_second(pos)
    op_start = str_time_to_second(op_start)
    op_end = str_time_to_second(op_end)
    video_len = str_time_to_second(video_len)
    if (op_start<=pos) and (pos<=op_end):
        pos = op_end


    for command in commands:
        if command == 'prev':
            pos -= 10
        elif command == 'next':
            pos += 10

