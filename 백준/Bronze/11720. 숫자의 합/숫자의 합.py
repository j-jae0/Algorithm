n = int(input())
nums = None
answer = None
num_list = None

# 숫자가 1개일 때
if n == 1:
    answer = int(input()) 
    print(answer)
else:
    num_list = list(input())
    num_list = [int(x) for x in num_list]
    print(sum(num_list))