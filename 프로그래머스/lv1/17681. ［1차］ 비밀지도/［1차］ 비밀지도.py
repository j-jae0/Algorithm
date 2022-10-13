# 숫자를 이진수로 바꾸는 함수
def to_bir(num, n):
    bir = []
    # 숫자를 이진수로 만드는 과정
    while True:          
        bir.insert(0, str(num % 2))
        num = num // 2
        print(bir)
        if num == 0:
            break  
            
    # 숫자 개수가 n개만큼 없다면 나머지를 0으로 채워줌
    if len(bir) != n:
        for i in range(n-len(bir)):
            bir.insert(0, str(0))
    # 이진수로 바꾼 것 문자열로 만들기
    return "".join(bir)

# 비밀지도 만드는 함수
def solution(n, arr1, arr2):
    answer = []
    bir1 = []
    bir2 = []
    # 각 리스트에 있는 숫자들을 이진수로 바꿔준다
    for num1, num2 in zip(arr1, arr2):
        bir1.append(to_bir(num1, n))
        bir2.append(to_bir(num2, n))

    # 만약 두 지도를 겹쳤을 때 하나라도 1이면 (문이 있으면) "#", 그 외엔 " "으로 만든다.
    num1_list = []
    for num1, num2 in zip(bir1, bir2):
        for i, j in zip(num1, num2):
            if i == '1' or j == '1':
                num1_list.append("#")
            else:
                num1_list.append(" ")
    
    # "#"와 " "를 n개씩 슬라이싱하여 문자열로 만들어준다
    answer = []
    for i in range(0, len(num1_list), n):
        answer.append("".join(num1_list[i:i+n]))

    return answer