def solution(my_string, is_suffix):
    real_suffix = [my_string[-i:] for i in range(1, len(my_string)+1)]
    return 1 if is_suffix in real_suffix else 0