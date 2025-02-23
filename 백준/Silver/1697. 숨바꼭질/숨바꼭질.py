# 1697
import sys
from collections import deque

def bfs(i):
    queue=deque()
    queue.append(i)
    visited[i]=0
    while queue:
        x=queue.popleft()
        if x == k:
            return visited[k]
        for i in (x+1, x-1, x * 2):
            if 0 <= i <= 100000 and not visited[i]: 
                visited[i] = visited[x] + 1
                queue.append(i)
        
n,k=map(int,sys.stdin.readline().split()) # 수빈, 동생
visited=[0]*(100000+1)

print(bfs(n))
