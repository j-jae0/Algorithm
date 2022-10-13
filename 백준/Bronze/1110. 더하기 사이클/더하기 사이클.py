"""
1) 숫자 받아오기 
2) 숫자가 1자리 수이면, 앞자리 0 붙여주기 
3) 숫자 분리 (앞자리, 뒷자리)
4) 숫자 더하고 앞자리, 뒷자리 다시 지정하기
5) 처음 숫자와 같은 숫자가 되면 반복 종료 (반복 횟수 출력)
"""

num = int(input())
num_list = [num//10, num%10]
last_num = 0
i = 0

start = True

while start:
    
    add_num = (num_list[-2] + num_list[-1]) % 10
    num_list.append(add_num)
    last_num = num_list[-2]*10 + num_list[-1]
    i += 1

    # 반복문 종료 시점
    if num == last_num:
        start = False
        
print(i)