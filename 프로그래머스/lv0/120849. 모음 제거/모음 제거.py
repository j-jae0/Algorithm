import re

def solution(my_string):
    answer = '[aeiou]'
    return re.sub(answer, "", my_string)