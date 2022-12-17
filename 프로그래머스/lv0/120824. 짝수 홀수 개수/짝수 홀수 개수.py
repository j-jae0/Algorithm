def solution(num_list):
    # 짝수 개수
    even_list = [e for e in num_list if e%2==0]
    even_cnt = len(even_list)
    # 홀수 개수
    odd_list = [o for o in num_list if o%2!=0]
    odd_cnt = len(odd_list)
    
    return [even_cnt, odd_cnt]