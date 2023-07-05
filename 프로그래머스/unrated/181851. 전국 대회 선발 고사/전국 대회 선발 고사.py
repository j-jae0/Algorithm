def solution(rank, attendance):
    dic = [(r, i) for i, r in enumerate(rank) if attendance[i]]
    top3 = sorted([d[0] for d in dic])[:3]
    idx = []
    for t in top3:
        for d in dic:
            if d[0] == t:
                idx.append(d[1])
    return 10000*idx[0] + 100*idx[1] + idx[2]