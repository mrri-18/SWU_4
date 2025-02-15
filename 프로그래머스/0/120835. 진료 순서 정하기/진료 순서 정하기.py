def solution(emergency):
    sorted_emergency = sorted(emergency, reverse=True)
    rank = {value: index + 1 for index, value in enumerate(sorted_emergency)}
    return [rank[k] for k in emergency]
