import sys
from collections import deque

n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]  # 인접 리스트 

# 간선 정보
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 차순으로 정렬 
for i in range(1, n + 1):
    graph[i].sort(reverse=True)

# BFS 함수
def bfs(start):
    visited = [False] * (n + 1)  
    order = [0] * (n + 1)       # 방문 순서 저장
    queue = deque([start])      # BFS 탐색을 위한 큐
    visited[start] = True
    count = 1                   # 방문 순서 카운터
    order[start] = count

    while queue:
        v = queue.popleft()     
        for w in graph[v]:      # 연결된 모든 노드 탐색
            if not visited[w]:  # 방문하지 않았다면
                count += 1
                visited[w] = True
                order[w] = count
                queue.append(w)

    return order

result = bfs(r)

# 출력
for i in range(1, n + 1):
    print(result[i])
