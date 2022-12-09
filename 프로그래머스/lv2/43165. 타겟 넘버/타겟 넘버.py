def solution(numbers, target):
    # 시작 0 -> [-n, n] -> ... 연결되는 방식으로 설정
    # 가정: numbers = [1, 2, 3] => 0 -> (-1, +1) ~ [-1, 1] -> (-2, +2) ~ [-3, +1, -1, +3] -> ....
    tree = [0]
    for num in numbers:
        new_node = []
        for t in tree:
            new_node.append(t+num)
            new_node.append(t-num)
        tree = new_node
    return tree.count(target)