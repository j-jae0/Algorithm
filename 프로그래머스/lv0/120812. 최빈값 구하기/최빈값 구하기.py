def solution(array):
    
    # 정수를 딕셔너리의 key 값으로 설정한다.
    arr_dict = {x: 0 for x in set(array)}
    val_list = []
    
    for a in array:
        arr_dict[a] += 1
    
    answer = 0
    for key, value in arr_dict.items():
        val_list.append(value)
        if answer < value:
            answer = value
    
    val_list = sorted(val_list, reverse=True)
    
    if len(val_list) != 1 and (val_list[0] == val_list[1]):
        return -1
    else:
        # key값과 value 값을 뒤집는다.
        r_arr_dict = dict(map(reversed, arr_dict.items()))
        return r_arr_dict[answer]
