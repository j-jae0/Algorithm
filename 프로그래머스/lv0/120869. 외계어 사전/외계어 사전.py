def solution(spell, dic):
    for d in dic:
        if sorted(spell) == sorted(d):
            return 1
    return 2
