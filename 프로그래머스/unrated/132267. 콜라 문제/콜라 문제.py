def solution(a, b, n):
    free_coke = 0
    while n >= a:
        free_coke += (n // a) * b
        n = n % a + (n // a) * b
    return free_coke