def solution(clothes):
    answer = 1
    
    type_clothes = [x[1] for x in clothes]
    type_num = len(set(type_clothes))
    dict_clothes = {}
    
    if type_num == 1:
        return len(clothes)
    else:
        for i in type_clothes:
            dict_clothes[i] = 0
            
        for c in clothes:
            dict_clothes[c[1]] += 1
            
        for val in dict_clothes.values():
            answer *= val + 1
            
        return answer-1