def solution(sides):
    answer_list = []
    # 가장 긴 변의 길이가 sides 리스트 내에 있는 경우
    max_length = max(sides)
    min_length = min(sides)
    new_length = list(range(1, max_length+1))
    
    for n in new_length:
        if min_length + n > max_length and n <= max_length:
            answer_list.append(n)
            
    # 가장 긴 변의 길이를 만드는 경우 
    total_length = sum(sides)
    answer_list.extend(list(range(max_length+1, total_length)))
    
    return len(set(answer_list))