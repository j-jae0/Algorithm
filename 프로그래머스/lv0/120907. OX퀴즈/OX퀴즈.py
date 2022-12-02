def solution(quiz):
    answer = []
    s_quiz = [q.split(" ") for q in quiz]
    for l in s_quiz:
        print(l)
        if l[1] == '-':
            if int(l[0]) - int(l[2]) == int(l[-1]):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if int(l[0]) + int(l[2]) == int(l[-1]):
                answer.append("O")
            else:
                answer.append("X")
                
    return answer