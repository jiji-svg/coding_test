# 재귀 함수
'''
1. 원판이 하나일때로 탈출 경로 만들어줌, 원판(n)=1 이면 [시작점, 도착지] 로 추가
2. 원판 n-1개를 가운데 기둥으로 놓기
3. 가장 큰 n을 마지막으로 옮기기
4. 가운데 기둥에 있는 n-1개를 마지막으로 옮기기.
'''


def solution(n, start=1, via=2, end=3):
    answer = []
    
    if n==1:
        return [[start, end]]
    
    answer += solution(n-1, start, end, via)
    answer.append([start, end])
    answer += solution(n-1, via, start, end)
    return answer
