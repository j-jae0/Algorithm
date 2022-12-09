def solution(answers):
    # 수포자 1, 2, 3의 정답리스트
    supoza = [[1, 2, 3, 4, 5],
              [2, 1, 2, 3, 2, 4, 2, 5],
              [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    
    # 수포자 1, 2, 3의 맞힌 문제 개수
    a_supoza = [0] * 3
    
    for i, a in enumerate(answers):
        for j, s in enumerate(supoza):
            if a == s[i % len(s)]:
                a_supoza[j] += 1

    return [i+1 for i, n in enumerate(a_supoza) if n == max(a_supoza)]