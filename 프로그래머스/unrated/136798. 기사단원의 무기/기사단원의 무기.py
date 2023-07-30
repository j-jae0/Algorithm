def solution(number, limit, power):
    prime = []
    for n in range(1, number+1):
        l = []
        for i in range(1, int(n**(1/2))+1):
            if n % i == 0:
                l.append(i) 
                if i ** 2 != n: 
                    l.append(n // i)
        prime.append(l)
    return sum([len(p) if len(p) <= limit else power for p in prime])