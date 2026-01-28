def solution(citations):
    citations.sort()
    n = len(citations)
    for i in range(n):
    # h_candidate: 현재 논문을 포함해 자신보다 많이 인용된 논문의 수
        h_candidate = n - i 
        if citations[i] >= h_candidate:
            return h_candidate
    return 0 # 모든 원소가 0인 경우
