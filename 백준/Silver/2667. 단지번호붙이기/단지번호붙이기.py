#2667 bfs 
import sys
from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(i,j,cnt):
    visited[i][j] = cnt
    queue=deque([[i,j]])
    size=1

    while queue:
        x,y=queue.popleft()
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k] 
            if 0 <= nx < n and 0 <= ny < n:
                if square[nx][ny] == 1 and visited[nx][ny]==0: # 방문한적이 없을 때
                    visited[nx][ny] = cnt
                    queue.append([nx,ny])
                    size+=1
                    
    return size

n=int(sys.stdin.readline())
square=[]
for _ in range(n):
    square.append(list(map(int,sys.stdin.readline().strip())))
visited=[[0]*n for _ in range(n)]
complex_size=[]
count =0
for i in range(n):
    for j in range(n):
        if square[i][j] == 1 and visited[i][j]==0 :
            count+=1
            complex_size.append(bfs(i,j,count))

print(count)
for i in sorted(complex_size):
    print(i)