from collections import Counter
def solution(participant, completion):
    counter=Counter(completion)
    player=Counter(participant)
    for i in counter.keys():
        if counter[i]!=player[i]: # 동명이인 처리
            return i
        else:
            del player[i]
    return list(player.keys())[0]