def solution(l, r):
    # set 으로 중복제거 후, 길이가 2 이하
    num_list = []
    condition = set(['0', '5'])
    
    for n in range(l, r+1):
        if n % 5 == 0 and len(set(str(n))-set(condition)) == 0:
            num_list.append(n)

    return num_list if len(num_list) >= 1 else [-1]