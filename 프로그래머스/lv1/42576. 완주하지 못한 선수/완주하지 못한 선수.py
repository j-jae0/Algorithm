def solution(participant, completion):
    completion.append('z'*20)
    zips = zip(sorted(participant), sorted(completion))
    return [z[0] for z in zips if z[0] != z[1]][0]