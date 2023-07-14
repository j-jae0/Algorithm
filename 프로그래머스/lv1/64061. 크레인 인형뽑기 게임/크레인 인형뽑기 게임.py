def solution(board, moves):
    doll = [0]
    answer = 0
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] != 0:
                if doll[-1] == board[i][m-1]:
                    doll.pop()
                    board[i][m-1] = 0
                    answer += 2
                else:
                    doll.append(board[i][m-1])
                    board[i][m-1] = 0
                break
    return answer