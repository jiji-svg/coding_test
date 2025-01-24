def solution(absolutes, signs):
    answer = 0
    for num, sign in zip(absolutes, signs):
        sym = '+' if sign else '-'
        answer += int(sym + str(num))
    return answer
