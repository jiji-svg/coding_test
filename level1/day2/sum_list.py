def solution(arr1, arr2):
    answer = arr1.copy()
    row_len = len(arr1[0])
    col_len = len(arr1)
    for i in range(col_len):
        for j in range(row_len):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer
