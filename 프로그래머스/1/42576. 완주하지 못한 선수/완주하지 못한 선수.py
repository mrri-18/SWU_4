from collections import Counter
def solution(participant, completion):
    player=Counter(participant)-Counter(completion)
    return list(player.keys())[0]