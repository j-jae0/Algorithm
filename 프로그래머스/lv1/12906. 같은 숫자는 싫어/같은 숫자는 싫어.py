# def solution(arr):
#     answer = []
#     a = 10 # 없는 숫자 넣어줌
    
#     for num in arr:        
#         if a != num:
#             answer.append(num)
#         else:
#             pass        
#         a = num
    
#     return answer

def solution(arr):
    answer = []
    a = 10
    
    for num in arr:        
        if a != num:
            answer.append(num)

        a = num
    
    return answer