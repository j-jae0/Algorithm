repeats = int(input())
ox = None

for i in range(repeats):
    """
    1) 받아온 OX 문자열을 리스트로 분리하기
    2) 리스트에서 첫번째 요소부터 마지막까지 분석할 것임 (반복문)
    3) 요소가 O이면 1 X이면 0, 새 리스트를 만들어 넣어줄 것임
    4) 요소가 O이면, 리스트에서 마지막 요소 list[-1]에 1을 더하여 넣어줄 것임 
    """
    ox = list(input())
    ox_list = [0]

    for i in ox:
        if i == 'O':
            ox_list.append(1 + ox_list[-1])
        elif i == 'X':
            ox_list.append(0)
    
    print(sum(ox_list))