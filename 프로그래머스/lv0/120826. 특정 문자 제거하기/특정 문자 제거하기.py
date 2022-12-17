import re

def solution(my_string, letter):
    
    # return my_string.replace(letter, "")
    return re.sub(letter, "", my_string)