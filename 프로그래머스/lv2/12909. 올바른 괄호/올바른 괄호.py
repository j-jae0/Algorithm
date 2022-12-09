def solution(s):
    """
    괄호가 열렸으면 무조건 닫혀야함
    ((())) 이런식으로 같은 괄호가 여러 번 반복될 수 있음
    열린 기호는 어느 경우에서도 올 수 있음 -> 끝에만 위치하지 않으면 됨
    닫힌 기호는 열린기호 뒤에만 올 수 있음 또는 닫힌 기호 뒤 -> 끝에 위치해야 함
    괄호 기호는 짝이 맞아야 함
    """
    s_list = []
    for b in s:
        if b == '(':
            s_list.append(b)
        # (, ) 가 만났을 때 ( 기호를 하나 를 뺀다. => 짝이 맞아야하기 때문
        elif b == ')' and len(s_list) >= 1:
            s_list.pop()
        else:
            return False
        
    return len(s_list) == 0