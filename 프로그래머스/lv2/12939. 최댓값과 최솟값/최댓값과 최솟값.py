def solution(s):
    """
    1) 문자열을 split으로 분리해주고 리스트에 넣는다.
    2) 반복문을 리스트의 길이만큼 돌린다.
    3) 리스트 안에 있는 요소를 int로 바꿔주고 min_num, max_num 변수에 리스트의 첫번째 요소로 넣는다.
    4) list안에 있는 요소들이 min_num으로 지정된 값보다 작은 경우, min_num을 그 값으로 지정 (최솟값)
    5) list안에 있는 요소들이 max_num으로 지정된 값보다 큰 경우, max_num에 그 값으로 지정 (최댓값)
    6) f-string으로 f"{최솟값} {최댓값}" 출력한다.
    """
    nums = list(map(int, s.split(" ")))
    min_num = nums[0]
    max_num = nums[0]
    
    for i in nums:
        if min_num > i:
            min_num = i
        
        if max_num < i:
            max_num = i

    return f"{min_num} {max_num}"
