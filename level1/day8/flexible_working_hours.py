def solution(schedules, timelogs, startday):
    answer = 0
    weekend = [0,6]
    event_days = [0 if (x%7) in weekend else 1 for x in range(startday, startday+7)]
    for scheduled_time, timelog in zip(schedules, timelogs):
        timelog = [x for x,y in zip(timelog, event_days) if (x*y)!=0]
        success = True
        hh, mm = int(str(scheduled_time)[:-2]), int(str(scheduled_time)[-2:])
        
        if (mm + 10) >= 60:
            hh += 1
            mm = (mm+10) % 60
        else:
            mm = mm+10
        scheduled_time = hh*100 + mm
        
        for commute_time in timelog:
            
            if commute_time > (scheduled_time):
                success = False
        if success:
            answer += 1
    
    return answer
