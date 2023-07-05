def solution(rank, attendance):
    rank_idx = [(r, i) for i, r in enumerate(rank) if attendance[i]]
    top3 = sorted([ri[0] for ri in rank_idx])[:3]
    idx = []
    for t in top3:
        for ri in rank_idx:
            if ri[0] == t:
                idx.append(ri[1])
    return 10000*idx[0] + 100*idx[1] + idx[2]