def solution(food):
    left = ''.join([str(i+1) for i, j in enumerate(food[1:]) for k in range(j//2)])
    right = left[::-1]
    return left + '0' + right