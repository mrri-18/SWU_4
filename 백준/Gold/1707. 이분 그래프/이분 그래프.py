import sys
sys.setrecursionlimit(10**6)  # 재귀 한도 증가
input = sys.stdin.readline

def dfs(node, color):
    visited[node] = color  # 현재 노드에 색깔 지정 (1 또는 -1)

    for w in graph[node]:  
        if visited[w] == 0:  
            if not dfs(w, -color):  # DFS 탐색
                return False  
        elif visited[w] == color:  # 이미 방문했는데 같은 색이면 이분 그래프 아님
            return False

    return True

# 입력 처리
total = int(input())  # 테스트 케이스 개수
for _ in range(total):
    m, n = map(int, input().split())  # 노드 수(m), 간선 수(n)
    
    graph = [[] for _ in range(m+1)]
    visited = [0] * (m+1)  # 색 정보를 저장하는 배열 (0: 방문X, 1: 색1, -1: 색2)
    is_bi = True  # 이분 그래프 여부

    # 간선 정보 입력 (양방향으로 저장해야 함)
    for _ in range(n):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)  # 양방향 그래프

    # 모든 노드에 대해 DFS 수행 (연결 요소가 여러 개일 수도 있음)
    for i in range(1, m+1):
        if visited[i] == 0:  # 방문하지 않은 정점에서 새로운 DFS 시작
            if not dfs(i, 1):  # 처음 시작하는 노드는 색깔 1
                is_bi = False
                break

    print("YES" if is_bi else "NO")
