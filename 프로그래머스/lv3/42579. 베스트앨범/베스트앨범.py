def solution(genres, plays):

    answer = []
    
    # 노래 장르별 총 재생 횟수 딕셔너리
    top_play = {g: 0 for g in genres}
    # 노래 장르별 재생횟수 및 인덱스 딕셔너리
    top_index = {g: [] for g in genres}

    # 딕셔너리의 value 값을 채움
    for i, (g, p) in enumerate(zip(genres, plays)):
        top_play[g] += p
        top_index[g].append((i, p))
    
    # 노래 장르별 총 재생 횟수를 내림차순으로 정렬
    for (k, v) in sorted(top_play.items(), key = lambda x:x[1], reverse=True):
        # 노래 장르에 대해 재생횟수가 높은 항목 2개 가져옴
        for (i, p) in sorted(top_index[k], key = lambda x:x[1], reverse=True)[:2]:
            answer.append(i)

    return answer