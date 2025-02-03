def solution(id_list, report, k):
    id_sets = set()
    reported_dict = {}
    reported_dict = dict.fromkeys(id_list, 0)
    
    for ids in report:
        reporter, reported = ids.split()
        if (reporter, reported) in id_sets:
            continue

        id_sets.add((reporter, reported))
        reported_dict[reported] += 1
    
    outs = []
    for key, value in reported_dict.items():
        if value >=k:
            outs.append(key)
    
    get_mail_dicts = dict.fromkeys(id_list, 0)
    id_lists = list(id_sets)
    for ids in id_lists:
        rep, reped = ids
        if reped in outs:
            get_mail_dicts[rep] += 1
    
    answer = []
    for value in get_mail_dicts.values():
        answer.append(value)
    
    
    # answer = 0
    return answer
