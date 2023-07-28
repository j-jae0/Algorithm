def solution(X, Y):
    if len(set(X) & set(Y)) == 0:
        return "-1"
    
    dic_x = {x:0 for i, x in enumerate(list(X))}
    dic_y = {y:0 for i, y in enumerate(list(Y))}
    xy = []
    for k in list(X): dic_x[k] += 1
    for k in list(Y): dic_y[k] += 1
    
    for k, v in dic_x.items():
        if k in dic_y.keys():
            for i in range(min([v, dic_y[k]])):
                xy.append(k)
    if len(set(xy)) == 1:
        return xy[0]
    return "".join(sorted(xy)[::-1])