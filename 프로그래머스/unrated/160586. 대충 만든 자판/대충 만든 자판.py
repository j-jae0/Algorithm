def solution(keymap, targets):
    keys = {k:100 for k in ''.join(keymap)}
    answer = []
    for key in keymap:
        for i, k in enumerate(list(key)):
            if keys[k] > i+1:
                keys[k] = i+1
    
    for target in targets:
        new_list = []
        for t in target:
            if t not in keys.keys():
                answer.append(-1)
                new_list = []
                break
            else:
                new_list.append(keys[t])
        if len(new_list):
            answer.append(sum(new_list))
    return answer