def solution(rny_string):
    return ''.join(['rn' if s == 'm' else s for s in rny_string])