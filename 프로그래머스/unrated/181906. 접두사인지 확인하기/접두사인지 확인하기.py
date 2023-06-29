def solution(my_string, is_prefix):
    real_prefix = [my_string[:i] for i in range(1, len(my_string)+1)]
    return 1 if is_prefix in real_prefix else 0