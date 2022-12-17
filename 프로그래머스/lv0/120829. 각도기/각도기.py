def solution(angle):
    # 예각 == 1, 직각 == 2, 둔각 == 3, 평각 == 4
    if 0 < angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif 90 < angle < 180:
        return 3
    elif angle == 180:
        return 4