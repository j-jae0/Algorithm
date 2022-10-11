h, m = map(int, input().split())

if m < 45:
# h = 0 또는 이상으로 나눔
    if h == 0:
        print(f"{h + 23} {m + 15}")
    else:
        print(f"{h - 1} {m + 15}")        
else:
    print(f"{h} {m - 45}")