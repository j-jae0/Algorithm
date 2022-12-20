def solution(numbers, direction):
    if direction == 'left':
        nums = numbers[1:]
        nums.append(numbers[0])
    else:
        nums = numbers[:-1]
        nums.insert(0, numbers[-1])
    return nums