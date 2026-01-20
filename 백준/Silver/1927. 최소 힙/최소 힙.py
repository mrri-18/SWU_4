import sys
import heapq

count=int(sys.stdin.readline())
heap=[]
heapq.heapify(heap)

for _ in range(count):
    tmp=int(sys.stdin.readline())
    if tmp==0:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,tmp)
    
