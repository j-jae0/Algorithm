# def solution(phone_book):

#     # 순서 정렬하여 접두사가 0번 위치에 있도록 설정
#     phone_book = sorted(phone_book)
    
#     # 접두사를 제외한 나머지 번호에서 접두사가 포함되었는지 확인
#     answer = True

#     for i in range(len(phone_book)-1):
#         if len(phone_book[i]) < len(phone_book[i+1]):
#             if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
#                 answer = False
#                 break

#     return answer
def solution(phone_book):

    # 순서 정렬하여 접두사가 0번 위치에 있도록 설정
    phone_book = sorted(phone_book)
    
    # 접두사를 제외한 나머지 번호에서 접두사가 포함되었는지 확인
    answer = True

    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
                return False
                break
        
    return True