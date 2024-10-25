def solution(order):
    answer = 0
    for coffee in order:
        if coffee.count('americano') or coffee.count('anything'):
            answer += 4500
        else:
            answer += 5000
    return answer
