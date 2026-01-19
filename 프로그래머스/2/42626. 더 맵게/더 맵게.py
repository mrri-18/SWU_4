import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0]<K: # 최소 스코빌이 k 이하인 동안
        if len(scoville)>=2 : # 음식 꺼내기 전 확인
            tmp1=heapq.heappop(scoville)
            tmp2=heapq.heappop(scoville)
            heapq.heappush(scoville,tmp1+(tmp2*2))
            answer+=1
        else: # K이상 합칠 수 없는 경우
            return -1
    
    return answer