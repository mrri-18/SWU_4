#7576
import sys
from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs():
    while queue:
        x,y=queue.popleft()
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k] 
            if 0 <= nx < m and 0 <= ny < n and square[nx][ny]==0:              
                square[nx][ny]=square[x][y]+1 # 가중치가 시간
                queue.append([nx,ny])
        
n,m=map(int,sys.stdin.readline().split())
square=[]
for _ in range(m):
    square.append(list(map(int,sys.stdin.readline().split())))
queue=deque()

for i in range(m):
    for j in range(n):
        if square[i][j]==1:
            queue.append((i,j))
bfs()

max_days = 0
for row in square:
    for tomato in row:
        if tomato == 0:  
            print(-1)
            exit()
        max_days = max(max_days, tomato)
print(max_days - 1)
