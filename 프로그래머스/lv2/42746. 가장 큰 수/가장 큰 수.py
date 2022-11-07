def solution(numbers):
    # 숫자를 문자열로 바꿔줌
    number = [str(num) for num in numbers]
    # 원소 범위 0 이상 1000 이하, 3자리수 처리
    # 만약, 앞자리가 같은 문자가 있다면 명확한 순서 비교를 위해 3자리수 처리
    # ex 10, 1 => 101010 111 => 111이 먼저올 수 있게 처리
    number = sorted(number,key=lambda x:x*3, reverse=True)
    
    return str(int("".join(number)))