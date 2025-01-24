def solution(participant, completion):
    participant = sorted(participant)
    completion = sorted(completion)
    length = len(completion)
    for idx in range(length):
        if participant[idx] != completion[idx]:
            return participant[idx]
    return participant[-1]
