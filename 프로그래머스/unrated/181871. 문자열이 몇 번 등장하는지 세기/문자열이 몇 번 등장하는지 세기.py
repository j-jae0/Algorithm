def solution(myString, pat):
    repeat = 0
    for i in range(len(myString)-len(pat)+1):
        if pat in myString[i:i+len(pat)]:
            repeat += 1
    return repeat