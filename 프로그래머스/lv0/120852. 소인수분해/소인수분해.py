def solution(n):
    """
    12 = 2*2*3 => 2가 두번 들어갈 수 있음
    특정 숫자에 대해 2회 이상 
    """
    answer = []
    num = n
    for i in range(2, n+1):
        for j in range(num//i):
            if num % i == 0:
                answer.append(i)
                num = int(num / i)
                
    return sorted(list(set(answer)))