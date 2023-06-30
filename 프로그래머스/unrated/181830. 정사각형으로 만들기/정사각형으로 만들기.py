def solution(arr):
    col = len(arr[0])
    row = len(arr)
    answer = arr
    
    if col == row:
        return arr
    elif col > row:
        for _ in range(col-row):
            answer.append([0 for _ in range(col)])
    elif col < row:
        for a in answer:
            for _ in range(row-col):
                a.append(0)
    return answer