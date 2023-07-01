def solution(num_list):
    answer = []
    
    for n in num_list:
        repeat = 0
        num = n
        while num != 1:
            if num % 2 == 0:
                num = num//2
                repeat += 1
            else:
                num = (num-1)//2
                repeat += 1
        answer.append(repeat)
    return sum(answer)