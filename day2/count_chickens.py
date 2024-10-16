def solution(chicken):
    service_chickens = chicken // 10
    remain_coupons = chicken % 10
    
    want_more = (service_chickens + remain_coupons)
    if want_more >= 10:
        service_chickens += solution(want_more)
    else:
        return service_chickens
    answer = service_chickens
    return answer

