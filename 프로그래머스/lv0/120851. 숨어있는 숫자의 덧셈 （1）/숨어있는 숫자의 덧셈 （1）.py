import re

def solution(my_string):
    answer = map(int, re.sub("[^0-9]", "", my_string))
    print(answer)
    return sum(answer)