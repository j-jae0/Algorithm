def solution(id_list, report, k):
    report = list(set(report))
    reported_dic = {i:0 for i in id_list}
    reporter_dic = {i:[] for i in id_list}
    for r in report:
        reporter = r.split()[0]
        reported = r.split()[-1]
        reported_dic[reported] += 1
        reporter_dic[reporter].append(reported)
    freeze_list = [i for i, v in reported_dic.items() if v >= k]
    
    mail_list = []
    for v in reporter_dic.values():
        n = 0
        if len(v) == 0:
            mail_list.append(n)
        else:
            for name in v:
                if name in freeze_list:
                    n += 1
            mail_list.append(n)
    return mail_list