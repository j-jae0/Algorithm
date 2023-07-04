def solution(myString, pat):
    if myString[-len(pat):] == pat: 
        return myString    
    idx = myString[::-1].index(pat[::-1])
    return myString[:-idx]