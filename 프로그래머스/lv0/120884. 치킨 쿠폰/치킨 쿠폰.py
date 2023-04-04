def solution(chicken):
    # 서비스로 먹을 수 있는 치킨의 수
    coupon = chicken
    service = 0
    
    while coupon >= 10:
        service += coupon // 10
        coupon = coupon % 10 + coupon // 10

    return service