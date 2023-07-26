def calculate_day(s):
    y, m, d = map(int, s.split("."))
    return y * 12 * 28 + m * 28 + d

def solution(today, terms, privacies):
    today = calculate_day(today)
    terms = {t.split()[0]: int(t.split()[1])*28 for t in terms}
    privacies = [[calculate_day(p.split()[0]), p.split()[1]] for p in privacies]
    expiry = [p[0] + terms[p[1]] - 1 for p in privacies]
    return [i+1 for i, e in enumerate(expiry) if e < today]