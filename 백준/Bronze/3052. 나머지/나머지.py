# 10개의 숫자를 받는다
nums = []
for i in range(10):
    nums.append(int(input()))

# 42로 나누고 나머지를 받는다
remainders = []
for num in nums:
    remainders.append(num % 42)

# 중복 제거 후 개수 반환
print(len(set(remainders)))