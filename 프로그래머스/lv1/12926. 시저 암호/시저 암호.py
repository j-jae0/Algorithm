def solution(s, n):
    l_alpha = 'abcdefghijklmnopqrstuvwxyz' * 2
    u_alpha = l_alpha.upper()
    answer = ''
    for alpha in s:
        if alpha == ' ':
            answer += alpha
        elif alpha in l_alpha:
            idx = l_alpha.index(alpha) + n
            answer += l_alpha[idx]
        elif alpha in u_alpha:
            idx = u_alpha.index(alpha) + n
            answer += u_alpha[idx]
    return answer