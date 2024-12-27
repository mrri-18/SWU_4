def bfs(board, start, goal, visited):
    n, m = len(board), len(board[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
    queue = deque([(start[0], start[1], 0)])  # (x, y, 이동 횟수)
    visited[start[0]][start[1]] = True

    while queue:
        x, y, count = queue.popleft()

        # 목표 지점에 도달했는지 확인
        if (x, y) == goal:
            return count

        # 네 방향으로 이동
        for dx, dy in directions:
            nx, ny = x, y
            # 벽에 부딪힐 때까지 이동
            while 0 <= nx + dx < n and 0 <= ny + dy < m and board[nx + dx][ny + dy] != 'D':
                nx += dx
                ny += dy
            
            # 멈춘 지점을 방문한 적 없다면 큐에 추가
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, count + 1))

    return -1  # 목표에 도달할 수 없음

from collections import deque

def solution(board):
    n, m = len(board), len(board[0])  
    visited = [[False] * m for _ in range(n)]  # 방문 배열
    start, goal = None, None

    # 시작점(R)과 목표점(G) 찾기
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start = (i, j)
            elif board[i][j] == 'G':
                goal = (i, j)

    # BFS 탐색
    return bfs(board, start, goal, visited)
