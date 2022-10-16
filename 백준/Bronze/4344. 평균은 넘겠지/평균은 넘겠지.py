repeats = int(input())

for i in range(repeats):
    scores = list(map(int, input().split()))
    score_list = scores[1:]
    score_avg = sum(score_list)/scores[0]
    student = 0

    for score in score_list:
        if score > score_avg:
            student += 1
    
    answer = (student/scores[0])*100
    print(f"{answer:.3f}%")