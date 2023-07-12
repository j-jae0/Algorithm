def solution(sizes):
    # 명함의 가장 긴 변을 가로 값으로, 가장 짧은 변을 세로 값으로 설정
    cards = [[max(s), min(s)] for s in sizes]
    max_w = max([c[0] for c in cards])
    max_h = max([c[1] for c in cards])
    return max_w * max_h