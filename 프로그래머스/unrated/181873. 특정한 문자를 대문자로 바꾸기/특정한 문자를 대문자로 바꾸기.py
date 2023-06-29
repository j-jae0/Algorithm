def solution(my_string, alp):
    new_string = []
    for s in my_string:
        if s == alp: new_string.append(s.upper())
        else: new_string.append(s)
    return ''.join(new_string)