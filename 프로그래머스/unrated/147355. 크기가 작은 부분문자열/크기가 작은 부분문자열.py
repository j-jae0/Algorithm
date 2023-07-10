def solution(t, p):    
    return len([j for j in [t[i:i+len(p)] for i in range(len(t)-len(p)+1)] if int(j) <= int(p)])