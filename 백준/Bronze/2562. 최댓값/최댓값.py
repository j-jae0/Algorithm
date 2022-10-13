nums = []
for i in range(9):
    nums.append(int(input()))

max_num = nums[0]
for i, num in enumerate(nums):
    if num > max_num:
        max_num = num

max_index = nums.index(max_num)
print(max_num)
print(max_index+1)