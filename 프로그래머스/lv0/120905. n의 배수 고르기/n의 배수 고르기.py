def solution(n, numlist):
    answer = []
    
    # 나누어 떨어지는 값만 리스트에 담기
    for num in numlist:
        if num % n == 0:
            answer.append(num)
            
    return answer