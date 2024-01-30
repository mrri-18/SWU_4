from collections import deque
def bfs(start):
    queue=deque([start])#자식에서 시작
    visited[start]=True
    while queue:#큐가 비어있지 않은 동안 반복
        v=queue.popleft()
        for i in graph[v]:#v와 연결된 점에 대한 반복문
            if not visited[i]:#visited가 false, 방문한적이 없다면 수행
                queue.append(i)#v와 연결된 점 중 방문하지 않은 점 방문
                res[i]=res[v]+1
                visited[i]=True

count=int(input())
m,n=map(int, input().split())
graph=[[] for _ in range(count+1)]
visited=[False]*(count+1)
res=[0]*(count+1)

for _ in range(int(input())):
    x,y=map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(m)
if res[n]>0:
    print(res[n])
else:
    print(-1)