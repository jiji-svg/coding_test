def solution(strings, n):
    ans = sorted(strings)
    answer = sorted(ans, key=lambda x:x[n])
    # tmp = []
    # for i, word in enumerate(strings):
    #     tmp.append((i, word[n], word))
    #     tmp.sort(key=lambda x:(x[1], x[2]))
    # for q in tmp:
    #     idx, key, _= q
    #     answer.append(strings[idx])
    return answer
