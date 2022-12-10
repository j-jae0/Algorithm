def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        new_list = []
        for j in range(n):
            new_list.append(num_list[i+j])
        answer.append(new_list)
        
    return answer