def solution(s, skip, index):
    alpha = [a for a in 'abcdefghijklmnopqrstuvwxyz'*3 if a not in skip]
    result = ''
    for ss in s:
        i = alpha.index(ss)
        result += alpha[i+index]
    return result