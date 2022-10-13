repeat_num = int(input())
nums = list(map(int, input().split()))
nums
min_num = nums[0]
max_num = nums[0]

for i in nums:
    if min_num > i:
        min_num = i
    if max_num < i:
        max_num = i

print(f"{min_num} {max_num}")