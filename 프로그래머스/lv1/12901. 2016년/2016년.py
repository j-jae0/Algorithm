from datetime import datetime

def solution(a, b):
    idx = datetime(2016, a, b).weekday()
    weeks = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return weeks[idx]