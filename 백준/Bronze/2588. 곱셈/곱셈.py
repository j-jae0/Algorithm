a = int(input())
b = int(input())
b_1 = b // 100
b_2 = (b%100)//10
b_3 = ((b%100)%10)

mult_1 = a * (b_3)
mult_2 = a * (b_2)
mult_3 = a * (b_1)
    
print(mult_1)
print(mult_2)
print(mult_3)
print(mult_1 + mult_2*10 + mult_3*100)