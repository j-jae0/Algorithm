from itertools import permutations


def solution(babbling):
    count = 0
    # 1, 2, 3, 4가지 경우에 대해 permutations 구하기
    basic_babblings = ["aya", "ye", "woo", "ma"]
    all_babblings = []
    for i in range(1, 5):
        perms = list(permutations(basic_babblings, i))

        for perm in perms:
            s = ''
            for element in perm:
                s += element
            all_babblings.append(s)

    for babblings in all_babblings:
        for babble in babbling:
            if babblings == babble:
                count += 1

    return count