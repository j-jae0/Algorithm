def solution(left, right):
    num_li = list(range(left, right+1))
    li = []
    for n in num_li:
        small_li = []
        for m in range(1, n+1):
            if n % m == 0:
                small_li.append(m)
                
        li.append(len(small_li))
    
    answer = 0
    for i, n in enumerate(li):
        if n % 2 == 0:
            answer += num_li[i]
        else:
            answer -= num_li[i]
            
    return answer