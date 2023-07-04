def solution(myString, pat):
    pat = ''.join(['A' if p == 'B' else 'B' for p in pat])
    return 1 if pat in myString else 0