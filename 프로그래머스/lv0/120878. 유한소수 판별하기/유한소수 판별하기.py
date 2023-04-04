def solution(a, b):
    # 기약분수 만들기 위해 최대공약수 구하기
    min_num = min([a, b])
    gcd = 0
    for n in range(1, min_num+1):
        if a % n == 0 and b % n == 0:
            gcd = n
    
    # 기약분수 형태로 만들기
    if gcd != 1:
        a = int(a/gcd)
        b = int(b/gcd)
    
    # 분모, 분자 같은 경우
    if a == b:
        return 1

    # 분모가 2, 5로만 이루어졌는지 확인하기
    num = b
    for i in [2, 5]:
        while num % i == 0:
            num //= i
        if num == 1:
            return 1

    return 2