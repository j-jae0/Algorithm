import math

# 최소 공배수 구하는 함수
def lcm(n,m):
    return (n*m) // math.gcd(n,m)

def solution(n, m):
    g = math.gcd(n,m)
    l = lcm(n,m)
    return [g, l]

        
    