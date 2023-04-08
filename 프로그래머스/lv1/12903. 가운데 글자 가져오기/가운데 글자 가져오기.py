def solution(s):
    idx = len(s)//2
    return s[idx-1:idx+1] if len(s) % 2 == 0 else s[idx]