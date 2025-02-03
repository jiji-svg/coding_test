def solution(keymap, targets):
    answer = []
#     for target in targets:
#         ans = 0
#         for alp in target:
#             min_idx = 101
            
#             for kmap in keymap:
                
#                 if alp in kmap:
                    
#                     idx = kmap.index(alp)
#                     min_idx = min(min_idx, idx)
                    
#             ans +=min_idx+1
#             if min_idx == 101:
#                 ans = -1
#                 break
            
#         answer.append(ans)
    hs = {}
    for k in keymap:
        for i, ch in enumerate(k):
            hs[ch] = min(i + 1, hs[ch]) if ch in hs else i + 1
    print(hs)
                    
    return answer
