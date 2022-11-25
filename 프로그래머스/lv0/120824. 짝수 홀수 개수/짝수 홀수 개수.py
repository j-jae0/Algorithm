def solution(num_list):
    
    return [len([x for x in num_list if x%2==0]), len([y for y in num_list if y%2!=0])]