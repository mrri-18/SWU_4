def solution(lottos, win_nums):
    zero_count = lottos.count(0)  
    win_nums = set(win_nums)  
    lottos = set(lottos) - {0}  # 0을 제외한 로또 번호 집합
    
    correct_count = len(lottos & win_nums)  # 맞춘 숫자 개수
    
    # 최고 등수와 최저 등수 계산
    highest_rank = min(7 - (correct_count + zero_count), 6)
    lowest_rank = min(7 - correct_count, 6)
    
    return [highest_rank, lowest_rank]
