def solution(today, terms, privacies):
    answer = []
    term_dict = {}
    today = today.replace('.', '')
    
    for term in terms:
        tp, mths = term.split()
        term_dict[tp] = int(mths)
    
    for i, privacy in enumerate(privacies,1):
        date, tp = privacy.split()
        y,m,d = map(int, date.split('.'))
        plus_month = term_dict[tp]
        m = m + plus_month
        d = d - 1
        while(m>12):
            y = y + 1
            m = m - 12
            
        if d == 0:
            m -= 1
            d = 28
        val_date = str(y) + str(m).zfill(2) + str(d).zfill(2)
        # print(privacy, val_date)
        if int(today) > int(val_date):
            answer.append(i)
        
            
        
    return answer
