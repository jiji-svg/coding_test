
def solution(num_list):
    last, sec_last = num_list[-1], num_list[-2]
    if last > sec_last:
        num_list.append(last-sec_last)
    else:
        num_list.append(last*2)
    return num_list
