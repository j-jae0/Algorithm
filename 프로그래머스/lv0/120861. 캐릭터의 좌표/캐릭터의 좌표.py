def solution(keyinput, board):
    ax0 = [x for x in range(board[0]//2*-1, board[0]//2+1)]
    ax1 = [y for y in range(board[1]//2*-1, board[1]//2+1)]
    
    x = 0 # 처음 좌표 (x)
    y = 0 # 처음 좌표 (y)
    
    for k in keyinput:
        
        if k == "left":
            if x <= ax0[0]:
                pass
            else:
                x -= 1
        elif k == "right":
            if x >= ax0[-1]:
                pass
            else:
                x += 1
        elif k == "up":
            if y >= ax1[-1]:
                pass
            else:
                y += 1
        elif k == 'down':
            if y <= ax1[0]:
                pass
            else:
                y -= 1
    
    return [x, y]