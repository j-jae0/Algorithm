def solution(my_string, indices):
    l = [s for i, s in enumerate(my_string) if i not in indices]
    return ''.join(l)