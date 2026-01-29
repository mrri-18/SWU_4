import heapq
def solution(scoville, K):
    count=0
    heapq.heapify(scoville)
    while scoville[0]<K:
        if len(scoville)>=2:
            tmp=heapq.heappop(scoville)
            second=heapq.heappop(scoville)
            heapq.heappush(scoville, tmp+second*2)
            count+=1
        else:
            return -1
    return count 