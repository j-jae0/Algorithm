def solution(s):
    total_text = ''
    idx = 0
    for text in s:
        if text == ' ':
            total_text += text
            idx = 0
            continue
        
        if idx % 2 == 0:
            total_text += text.upper()
            idx += 1
        else:
            total_text += text.lower()
            idx += 1
    return total_text