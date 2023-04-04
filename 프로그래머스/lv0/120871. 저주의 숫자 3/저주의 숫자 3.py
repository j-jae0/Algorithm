def solution(n):
    town = []
    for i in range(1, n*3):
        if i % 3 == 0 or '3' in str(i):
            pass
        else:
            town.append(i)
        if len(town) == n:
            break
      
    return town[n-1]