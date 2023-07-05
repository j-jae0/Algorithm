import re

def solution(myStr):
    myStr = re.sub('a|b|c', ' ', myStr).strip()
    return myStr.split() if len(myStr) > 0 else ['EMPTY']