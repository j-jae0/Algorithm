def solution(park, routes):
    x, y = [[j, i] for i, p in enumerate(park) for j, s in enumerate(p) if s == 'S'][0]
    for route in routes:
        direc, steps = route.split()
        new_x, new_y = x, y
        # 방향별로 공원을 벗어나면 안되고 장애물을 만나선 안된다.
        for step in range(int(steps)):
            if direc == 'E' and new_x != len(park[0])-1 and park[new_y][new_x+1] != 'X':
                new_x += 1
                if step == int(steps)-1:
                    x = new_x
            elif direc == 'W' and new_x != 0 and park[new_y][new_x-1] != 'X':
                new_x -= 1
                if step == int(steps)-1:
                    x = new_x
            elif direc == 'S' and new_y != len(park)-1 and park[new_y+1][new_x] != 'X':
                new_y += 1
                if step == int(steps)-1:
                    y = new_y
            elif direc == 'N' and new_y != 0 and park[new_y-1][new_x] != 'X':
                new_y -= 1
                if step == int(steps)-1:
                    y = new_y
    return [y, x]