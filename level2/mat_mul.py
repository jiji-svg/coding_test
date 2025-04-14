def solution(arr1, arr2):
    import numpy as np
    ar1, ar2 = np.array(arr1), np.array(arr2)
    # answer = np.matmul(ar1, ar2)
    answer = np.dot(ar1, ar2)
    answer = answer.tolist()
    return answer
