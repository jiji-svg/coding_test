def solution(arr):
    answer = []
    
    cnt_row = len(arr)
    cnt_col = len(arr[0])
    if cnt_row > cnt_col:
        for tmp_list in arr:
            i = 0
            while (cnt_row > cnt_col + i):
                tmp_list.append(0)
                i += 1
            answer.append(tmp_list)
    
    elif cnt_row < cnt_col:

