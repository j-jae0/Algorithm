# 과목 개수
n = int(input())

# 시험 성적 입력
scores = list(map(int, input().split()))
# 높은 점수 max_score로 지정
max_score = max(scores)

# 점수 속이기
new_scores = 0

for score in scores:
    new_scores += (score/max_score)*100

print(new_scores/n)