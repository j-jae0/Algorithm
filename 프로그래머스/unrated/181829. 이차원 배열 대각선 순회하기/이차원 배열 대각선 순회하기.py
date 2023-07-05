def solution(board, k):
    answer = 0
    for i, b in enumerate(board):
        for j in range(len(b)):
            if i+j <= k:
                answer += board[i][j]
    return answer