def solution(myString):
    myString = myString.lower()
    newString = ''
    for s in myString:
        if s == 'a': newString += 'A'
        else: newString += s
    return newString