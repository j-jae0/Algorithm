import statistics

def solution(score):
    # 평균값을 리스트에 담는다.
    mean_score = [statistics.mean(scores) for scores in score]
    # 평균값을 정렬한다.(내림차순)
    s_mean_score = sorted(mean_score, reverse=True)
    
    # 등수 리스트
    answer = []
    for m in mean_score:
        answer.append(s_mean_score.index(m) + 1)
        
    return answer