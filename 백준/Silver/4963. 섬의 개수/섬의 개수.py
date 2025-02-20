#2667 bfs 
import sys
from collections import deque

dx=[1,-1,0,0,-1,-1,1,1]
dy=[0,0,1,-1,-1,1,-1,1]

def bfs(i,j):
    visited[i][j] = 1
    queue=deque([[i,j]])
    local_count=1

    while queue:
        x,y=queue.popleft()
        for k in range(8):
            nx=x+dx[k]
            ny=y+dy[k] 
            if 0 <= nx < h and 0 <= ny < w:
                if square[nx][ny] == 1 and visited[nx][ny]==0: # 방문한 적이 없을 때
                    visited[nx][ny] = 1
                    queue.append([nx,ny])

while True:
    w,h=map(int,sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    square=[]
    for _ in range(h):
        square.append(list(map(int,sys.stdin.readline().split())))
    visited=[[0]*w for _ in range(h)]
    count =0
    complex_size=[]
    for i in range(h):
        for j in range(w):
            if square[i][j] == 1 and visited[i][j]==0 :
                count+=1
                complex_size.append(bfs(i,j))
    print(count)

