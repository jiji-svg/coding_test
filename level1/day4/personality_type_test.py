def solution(survey, choices):
    answer = ''
    names = ['A', 'N', 'C','F','R','T','M','J']
    together_names = ['RT', 'CF', 'JM', 'AN']
    dict_names = dict.fromkeys(names, 0)
    for s, c in zip(survey, choices):
        f, l = s[0], s[1]
        if c>=4:
            dict_names[l] += c-4
        else:
            dict_names[f] += 4-c
    
    
    for name in together_names:
        n1, n2 = name
        
        if dict_names[n1] > dict_names[n2]:
            answer += n1
        elif dict_names[n1] < dict_names[n2]:
            answer += n2
        else:
            answer += n1
    
    return answer
