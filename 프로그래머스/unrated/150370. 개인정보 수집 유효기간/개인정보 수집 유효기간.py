def solution(today, terms, privacies):
    privacies = [p.split() for p in privacies]
    terms = {t.split()[0]: int(t.split()[1]) for t in terms}
    expiry = []
    
    for p in privacies:
        join_year, join_month, join_date = p[0].split(".")
        months = terms[p[1]]
        if join_date == "01":
            join_date = "28"
            join_month = int(join_month) - 1
        else:
            join_date = str(int(join_date) - 1)
        join_month = int(join_month) + months
        if join_month % 12 == 0 and join_month > 12:
            join_year = str(int(join_year) + (join_month - 12)//12)
            join_month = "12"
        elif join_month % 12 == 0:
            join_month = "12"
        else:
            join_year = str(int(join_year) + int(join_month) // 12)
            join_month = str(join_month % 12)
        if len(join_month) < 2:
            join_month = "0" + join_month
        if len(join_date) < 2:
            join_date = "0" + join_date
        
        expiry_date = join_year + "." + join_month + "." + join_date
        expiry.append(expiry_date)
    return [i+1 for i, e in enumerate(expiry) if e < today]