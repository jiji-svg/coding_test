def solution(wallpaper):
    answer = []
    rows = []
    cols = []
    
    for ri, pap in enumerate(wallpaper):
        while('#' in pap):
            rows.append(ri)
            ci = pap.index('#')
            cols.append(ci)
            if ci == len(pap):
                pap = pap[:ci]
            else:
                pap = pap[:ci] + '.' + pap[ci+1:]
    answer.append(min(rows))
    answer.append(min(cols))
    answer.append(max(rows)+1)
    answer.append(max(cols)+1)
    return answer
