def solution(myString):
    l = filter(None, myString.split('x'))
    return sorted(l)