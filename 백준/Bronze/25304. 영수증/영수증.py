# 영수증에 적힌 지불 가격
total_bills = int(input())
# 주문한 음식 개수
count_foods = int(input())
# 주문 확인하기
total = 0

for i in range(1, count_foods+1):
    price, count = map(int, input().split())
    total += (price * count)
    
if total == total_bills:
    print("Yes")
else:
    print("No")