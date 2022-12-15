def solution(n):
    """
    합성수는 1과 본인을 제외하고 다른 값으로 나눠질 수 있는 수를 말한다.
    ex) 2 = 1*2 (소수) / 4 = 1*4, 2*2 (합성수)
    """
    answer = []
    cnt_answer = 0
    
    for num1 in range(2, n+1):
        for num2 in range(1, num1+1):
            if num1%num2 == 0:
                answer.append(num1)
     
        if answer.count(num1) > 2:
            cnt_answer += 1
            
    return cnt_answer