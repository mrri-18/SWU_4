def solution(citations):
    answer = 0
    citations.sort(reverse = True) 
    for num, citation in enumerate(citations):
        # 피인용수가 더 작다가 -> 크거나 같아지는 시점 
        if citation >= num+1: 
            answer=num+1

    return answer