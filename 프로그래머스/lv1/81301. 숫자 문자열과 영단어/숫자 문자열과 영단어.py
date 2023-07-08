def solution(s):
    en_num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", 'nine']
    for i, e in enumerate(en_num):
        s = s.replace(e, str(i))
    return int(s)