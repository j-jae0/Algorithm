n, x = map(int, input().split())
list_nums = list(map(int, input().split()))
bigger_nums = []
    
for i in list_nums:
    if x > i:
        bigger_nums.append(str(i))

print(" ".join(bigger_nums))