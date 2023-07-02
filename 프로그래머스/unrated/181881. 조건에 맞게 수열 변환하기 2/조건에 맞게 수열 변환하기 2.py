def solution(arr):
    case = [[0], arr]
    repeat = 0
    while case[-1] != case[-2]:
        new_arr = []
        for n in case[-1]:
            if n >= 50 and n % 2 == 0:
                new_arr.append(n//2)
            elif n < 50 and n % 2 != 0:
                new_arr.append(n*2+1)
            else:
                new_arr.append(n)
        case.append(new_arr)
        repeat += 1
    return repeat-1