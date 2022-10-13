h, m = map(int, input().split())
c = int(input())

add_h = (m + c) // 60
add_m = (m + c) % 60

total_h = h + add_h
total_m = add_m

if total_h >= 24:
    total_h = total_h % 24
    
print(f"{total_h} {total_m}")