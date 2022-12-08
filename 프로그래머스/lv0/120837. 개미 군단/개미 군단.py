def solution(hp):
    fir = hp // 5
    sec = (hp - fir*5)//3
    thr = (hp - fir*5 - sec*3)//1
    return fir + sec + thr