def solution(board, k):
    # answer = 0
    # for i, b in enumerate(board):
    #     for j in range(len(b)):
    #         if i+j <= k:
    #             answer += board[i][j]
    return sum([board[i][j] for i in range(len(board)) for j in range(len(board[i])) if i+j <=k])