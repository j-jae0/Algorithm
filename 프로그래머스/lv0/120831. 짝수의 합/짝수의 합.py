def solution(n):
#     answer = []
    
#     # 2부터 n까지의 숫자를 스텝을 2로 하여 변수에 추가
#     for i in range(2, n+1, 2):
#         answer.append(i)
    
#     return sum(answer)
    return sum([x for x in range(n+1) if x%2==0])