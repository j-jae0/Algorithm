def solution(board):
    n = len(board)
    b = [[0 for i in range(n+2)] for j in range(n+2)]
    m = len(b)
    new_b = []

    # 폭탄 심기
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for k in range(i, i+3):
                    for h in range(j, j+3):
                        b[k][h] = 1
    # 정렬 다시 재정렬
    for n in b[1:-1]:  
        new_b.append(n[1:-1])
        
    # 정답값
    answer = 0
    for i in range(len(new_b)):
        for j in range(len(new_b)):
            if new_b[i][j] == 0:
                answer += 1
                
    return answer