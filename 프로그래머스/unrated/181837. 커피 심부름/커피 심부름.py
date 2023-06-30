def solution(order):
    menu = {'americano': 4500, 
            'cafelatte': 5000, 
            'anything': 4500}
    
    # hot, ice 제거하기(가격동일)
    remove_hot = [o.replace('hot', '')  for o in order]
    remove_sub = [o.replace('ice', '')  for o in remove_hot]
    
    return sum([menu[o] for o in remove_sub])