def solution(arr):
    stk = []
    for i in range(len(arr)):
        if arr[i] not in stk:
            stk.append(arr[i])
        else:
            if arr[i] == stk[-1]:
                stk.pop(-1)
            else:
                stk.append(arr[i])
    if stk == []:
        stk = [-1]
    return stk
