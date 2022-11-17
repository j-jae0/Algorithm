def solution(denum1, num1, denum2, num2):
    # 최소공배수 구하기 (예: 2, 4 => 2 * 1* 2 == 4, [2, 3, 5, 7, 11, 13, ... 소수])
    r_num = num1 * num2
    r_denum = denum1*num2 + denum2*num1

    for i in range(r_denum, 1, -1):
        if r_num%i == 0 and r_denum%i == 0:
            return [r_denum//i, r_num//i]
    
    return [r_denum, r_num]