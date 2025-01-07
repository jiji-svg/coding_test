def solution(arr):
    answer = [arr[0]]
    for num in arr:
        if answer[-1] == num:
            continue
        else:
            answer.append(num)
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print('Hello Python')
    return answer
