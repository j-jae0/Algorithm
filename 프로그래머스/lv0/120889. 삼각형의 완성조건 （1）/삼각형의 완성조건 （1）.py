def solution(sides):
    sorted_sides = sorted(sides, reverse=True)
    large_s = sorted_sides[0]
    other_sum_s = sum(sorted_sides[1:])
    
    return 2 if large_s >= other_sum_s else 1