def solution(price, money, count):
    n_money = 0
    
    # 놀이기구 이용 시 필요한 금액
    for n in range(1, count+1):
        n_money += (price * (n))

    if money >= n_money:
        return 0
    else:
        return n_money - money
