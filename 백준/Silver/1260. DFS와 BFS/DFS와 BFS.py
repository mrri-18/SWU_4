#1260

import sys
from collections import deque

def dfs(index):
    visited[index] = True
    print(index, end=' ')
    for w in sorted(graph[index]):
        if not visited[w]:
            dfs(w)

def bfs(start):
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        print(v, end=' ')
        for i in sorted(graph[v]): # 오름차순 구현
            if not visited[i]:
                visited[i] = True
                queue.append(i)


m,n,start=map(int, sys.stdin.readline().split())
graph=[[] for _ in range(m+1)]
visited=[False]*(m+1)

for _ in range(n): # 입력
    a,b=map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(start)
print('')
visited=[False]*(m+1) # 같은 visited를 쓸 수 없음.
bfs(start)