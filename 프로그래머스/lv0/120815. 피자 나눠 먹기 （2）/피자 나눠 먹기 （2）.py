def solution(n):

    for i in range(1, n*6+1):
        if (i*6)%n == 0:
            return i
            break

