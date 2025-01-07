from datetime import datetime
def solution(a, b):
    # 2016.01.01은 금요일
    datestr1 = '2016-01-01'
    datestr2 = '2016-'+str(a)+'-'+str(b)
    date1 = datetime.strptime(datestr1, "%Y-%m-%d")
    date2 = datetime.strptime(datestr2, "%Y-%m-%d")
    diff = (date2-date1).days
    # m_num = int(m_num)
    diff = diff % 7
    weeks = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    answer = weeks[diff]
    
    
    return answer
