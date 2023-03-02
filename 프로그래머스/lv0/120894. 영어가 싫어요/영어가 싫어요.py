def solution(numbers):
    words_3 = {"one":"1", "two":"2", "six":"6"}
    words_4 = {"zero":"0", "four":"4", "five":"5", "nine":"9"}
    words_5 = {"three":"3", "seven":"7", "eight":"8"}
    num = numbers
    answer = ""
    for _ in range(len(numbers)//3):
        if num[:3] in words_3.keys():
            answer += words_3[num[:3]]
            num = num[3:]
        elif num[:4] in words_4.keys():
            answer += words_4[num[:4]]
            num = num[4:]
        elif num[:5] in words_5.keys():
            answer += words_5[num[:5]]
            num = num[5:]    
    return int(answer)