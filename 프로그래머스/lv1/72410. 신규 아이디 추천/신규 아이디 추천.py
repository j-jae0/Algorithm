import re

def solution(new_id):    
    # 1단계 : 모든 대문자 -> 소문자 치환
    new_id = new_id.lower()
    # 2단계 : 소문자, 숫자, -, _, . 만 남기기
    pattern = '[^a-z|0-9|\-\_\.]'
    new_id = re.sub(pattern, "", new_id)
    # 3단계 : .가 2번 이상 연속 부분은 하나로 치환
    for _ in range(len(new_id)-1):
        new_id = new_id.replace("..", ".")
    # 4단계 : .가 처음이나 끝에 위치하면 제거 - 두 조건 다 만족할 수 있으니 if문 두개 넣어버림
    new_id = new_id[1:] if new_id[0] == '.' and len(new_id) > 1 else new_id
    new_id = new_id[:-1] if new_id[-1] == '.' else new_id
    # 5단계 : 빈 문자열이라면 a 대입
    new_id = 'a' if len(new_id) == 0 else new_id
    # 6단계 : 16자 이상이면 15자만 가져오고 나머지 제거 (제거 후 마침표가 끝에 위치하면 제거)
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    # 7단계 : 길이가 2자 이하라면 마지막 문자를 길이가 3이 될 때까지 반복하여 채우기
    if len(new_id) <= 2:
        last_str = new_id[-1]
        for _ in range(3-len(new_id)):
            new_id += last_str
    return new_id

