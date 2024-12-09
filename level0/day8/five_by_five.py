def solution(names):
    # answer = [name for i,name in enumerate(names) if i%5==0]
    answer = names[::5]
    return answer
