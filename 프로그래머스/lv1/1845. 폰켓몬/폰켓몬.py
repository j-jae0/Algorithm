# def solution(nums):
#     # 가질 수 있는 포켓몬 수
#     get_num = int(len(nums)/2)
    
#     # 중복 제거하였을 때, 종류가 몇 개인지 확인
#     set_nums = set(nums)
#     set_num = len(set_nums)
    
#     # 폰켓몬 종류 수의 최댓값
#     answer = 0
    
#     if get_num >= set_num:
#         answer = set_num
#     else:
#         answer = get_num
    
#     return answer
def solution(nums):
    
    if int(len(nums)/2) >= len(set(nums)):
        return len(set(nums))
    else:
        return int(len(nums)/2)
