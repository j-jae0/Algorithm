def solution(num):
    """
    1. 입력된 수가 짝수이면 2를 나눈다.
    2. 입력된 수가 홀수라면 3을 곱하고 1을 더한다.
    3. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복한다.
    ==> 반복은 1이 될 때까지 진행된다.
    4. 주어진 수가 1인 경우, 0을 반환
    5. 작업이 500번 반복할 때까지 1이 되지 않으면 -1을 반환
    """
    repeat_num = 0
    last_num = num
    
    # 주어진 값이 1인 경우를 먼저 고려 함
    if last_num == 1:
        return 0
    
    # 반복된 횟수를 repeat_num에 지정 함
    while last_num != 1:
        
        # 반복 횟수가 500번 되면 stop
        if repeat_num == 500:
            return -1
        
        # 입력받은 값이 짝수, 홀수 케이스 나눠서 처리
        if last_num % 2 == 0:
            last_num = last_num/2
        else:
            last_num = (last_num*3)+1
        
        repeat_num += 1

    return repeat_num
    
    