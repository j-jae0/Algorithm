def solution(numbers):
    num_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, n in enumerate(num_list):
        numbers = numbers.replace(n, str(i))
    return int(numbers)