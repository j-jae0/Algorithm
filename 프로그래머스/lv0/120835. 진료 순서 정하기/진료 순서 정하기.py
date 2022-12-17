def solution(emergency):
    ordered_e = sorted(emergency, reverse=True)
    return [ordered_e.index(n)+1 for n in emergency]
