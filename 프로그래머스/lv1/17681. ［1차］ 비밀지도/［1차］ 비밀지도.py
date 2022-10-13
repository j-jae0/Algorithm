def to_bir(num, n):
    bir = []
    while True:          
        bir.insert(0, str(num % 2))
        num = num // 2
        print(bir)
        if num == 0:
            break  
    if len(bir) != n:
        for i in range(n-len(bir)):
            bir.insert(0, str(0))
    return "".join(bir)

def solution(n, arr1, arr2):
    answer = []
    bir1 = []
    bir2 = []
    for num1, num2 in zip(arr1, arr2):
        bir1.append(to_bir(num1, n))
        bir2.append(to_bir(num2, n))
        print(bir1)
        print(bir2)

    num1_list = []
    for num1, num2 in zip(bir1, bir2):
        for i, j in zip(num1, num2):
            if i == '1' or j == '1':
                num1_list.append("#")
            else:
                num1_list.append(" ")
    answer = []
    for i in range(0, len(num1_list), n):
        answer.append("".join(num1_list[i:i+n]))

    return answer
