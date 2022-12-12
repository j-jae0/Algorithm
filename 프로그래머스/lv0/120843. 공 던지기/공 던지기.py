def solution(numbers, k):
    idx = (2*(k-1)) % len(numbers)
    return numbers[idx]

# +2 * (5-1) => 8 % 6 => 2
# +2 * 1 => 2 % 3 => 2