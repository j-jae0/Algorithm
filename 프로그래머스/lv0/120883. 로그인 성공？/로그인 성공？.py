def solution(id_pw, db):
    if id_pw in db:
        return 'login'
    else:
        answer = 'fail'
        for data in db:
            if id_pw[0] == data[0] and id_pw[1] != data[1]:
                return 'wrong pw'
        return 'fail'