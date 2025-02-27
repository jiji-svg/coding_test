from itertools import combinations as c
def solution(n, q, ans):
    answer = 0
    answer_coms = list(c(range(1, n+1), 5))

    for nums, a in zip(q, ans):
        tmp_coms = []
        for code in answer_coms:
            if len(set(code)&set(nums)) == a:
                tmp_coms.append(code)
        answer_coms = tmp_coms.copy()
    answer = len(answer_coms)
    return answer
# import itertools 

# def solution(n, q, ans):
#     f = list(itertools.combinations(range(1, n + 1), 5))

#     for g, cnt in zip(q, ans):
#          f = [code for code in f if len(set(code) & set(g)) == cnt]

#     return len(f)
