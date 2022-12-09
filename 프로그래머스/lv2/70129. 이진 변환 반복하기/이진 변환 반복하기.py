def solution(s):
    """
    1. 0 제거
    2. 남은 1의 개수를 변수 l에 저장
    3. l을 이진변환했을 때 1이될 때까지 카운트해야 함 + 제거한 총 0의 개수
    """
    # 첫 번째 값 : 횟수, 두 번째 값 : 제거한 0의 개수 
    answer = [0] * 2
    num = s
    while num != '1':
        answer[1] += num.count("0")
        num = num.replace("0", "")
        num = bin(int(len(num)))[2:]        
        answer[0] += 1
    
    return answer
