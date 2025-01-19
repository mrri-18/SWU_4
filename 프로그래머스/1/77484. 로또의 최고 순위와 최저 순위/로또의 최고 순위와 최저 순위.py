def solution(lottos, win_nums):
    zero_count=lottos.count(0)
    remove_set = {0}
    lottos = [i for i in lottos if i not in remove_set]
    
    lottos=set(lottos)
    if len(lottos)==0: return [1,6]
    win_nums=set(win_nums)
    count=len(lottos & win_nums) # 맞춘 개수

    return [7-(count+zero_count) if count > 0 else 6, 7-count if count > 0 else 6] # 0이 맞음, 0이 틀림 