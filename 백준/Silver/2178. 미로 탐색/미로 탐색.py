import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j):
    queue = deque([[i, j]])
    visited[i][j] = 1  # 시작 위치 방문 표시

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if square[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    square[nx][ny] = square[x][y] + 1  # 이전 위치의 값에 1을 더해 경로 길이 저장
                    queue.append([nx, ny])

n, m = map(int, sys.stdin.readline().split())
square = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

bfs(0, 0)
print(square[n-1][m-1])  # 도착 지점의 값 출력
