import numpy as np

def solution(n):
    l = []
    for i in range(2, n+1):
        prime = True
        for j in range(2, int(np.sqrt(i))+1):
            if i % j == 0:
                prime = False
                break
        if prime:
            l.append(i)
    return len(l)