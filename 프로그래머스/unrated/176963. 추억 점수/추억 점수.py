def solution(name, yearning, photo):
    answer = []
    for one_photo in photo:
        memory_point = 0
        for person in one_photo:
            if person in name:
                memory_point += yearning[name.index(person)]
        answer.append(memory_point)
    return answer