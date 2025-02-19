#1260

import sys
from collections import deque

# def dfs(index):
#     visited[index] = True
#     print(index, end=' ')
#     for w in sorted(graph[index]):
#         if not visited[w]:
#             dfs(w)

def bfs(start):
    global count
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if not visited[i]: # 방문한적이 없을 때
                visited[i] = True
                queue.append(i)
            else:
                continue

m,n=map(int, sys.stdin.readline().split())
graph=[[] for _ in range(m+1)]

for _ in range(n): # 입력
    a,b=map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

count=0
visited=[False]*(m+1) 
for i in range(1, m+1):
    if not visited[i]: # 방문한 노드는 다시 탐색할 필요 없음
        bfs(i)
        count+=1

print(count)