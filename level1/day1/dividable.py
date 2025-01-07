def solution(arr, divisor):
    answer = sorted([x for x in arr if x%divisor==0]) or [-1]
    # if not answer:
    #     answer=[-1]
    return answer
