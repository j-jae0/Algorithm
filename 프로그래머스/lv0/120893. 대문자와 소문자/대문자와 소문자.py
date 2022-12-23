import re

def solution(my_string):
    answer = ""
    for s in my_string:
        l = re.sub("[a-z]", "", s)
        u = re.sub("[A-Z]", "", s)
        if len(l) == 0:
            answer += s.upper()
        else: answer += s.lower()
    return answer
            