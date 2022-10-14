def solution(participant, completion):
    """
    1) 참가자 명단에는 완주자 명단보다 1명 더 많다.
    2) for문과 remove 를 같이 쓰면 효율이 떨어진다.    
    3) 동명이인이 있을 수 있다. -> set으로 차집합, if not in 적합하지 않다.
    """
    
    part = sorted(participant)
    comp = sorted(completion)
    answer = part[-1]

    for i in range(len(comp)):
        if part[i] == comp[i]:
            pass
        elif part[i] != comp[i]:
            answer = part[i]
            break

    return answer
        