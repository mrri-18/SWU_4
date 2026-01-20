from collections import Counter
def solution(participant, completion):
    p_count=Counter(participant) # 딕셔너리
    c_count=Counter(completion)
    for i in participant:
        if p_count[i]==c_count[i]:
            pass
        else:
            return i
        