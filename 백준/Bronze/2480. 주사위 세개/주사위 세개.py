# 주사위 세 개 값 받아오기
a, b, c = map(int, input().split())

list_num = [a, b, c]
same_num = 0
bigger_num = 0

if (a == b) and (b == c):
    print(10000 + a*1000)
elif (a == b) or (b == c) or (a == c):
    if a == b:
        same_num = a
    elif b == c:
        same_num = b
    elif a == c:
        same_num = c
    print(1000 + same_num*100)
elif (a != b) and (b != c) and (a != c):
    for num in list_num:
        if num > bigger_num:
            bigger_num = num
    print(100*bigger_num)   