def solution(before, after):
    bf_dict = {}
    af_dict = {}
    for n in before:
        if n not in bf_dict.keys():
            bf_dict[n] = 1
        else:
            bf_dict[n] += 1
            
    for m in after:
        if m not in af_dict.keys():
            af_dict[m] = 1
        else:
            af_dict[m] += 1
    
    if sorted(bf_dict.keys()) == sorted(af_dict.keys()):            
        for k, v in bf_dict.items():
            if bf_dict[k] != af_dict[k]:
                return 0
        return 1
    else:
        return 0
    
    