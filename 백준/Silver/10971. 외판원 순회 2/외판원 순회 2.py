import sys

def dfs(current, visited, cost_sum):
    global min_cost

    # 모든 도시를 방문한 경우
    if len(visited) == n:
        # 마지막 도시에서 시작점으로 돌아갈 수 있는지 확인
        if array[current][0] != 0:
            min_cost = min(min_cost, cost_sum + array[current][0])
        return

    # 다른 도시로 이동
    for next_city in range(n):
        if next_city not in visited and array[current][next_city] != 0:
            # 방문 표시와 비용 추가
            visited.add(next_city)
            dfs(next_city, visited, cost_sum + array[current][next_city])
            visited.remove(next_city)

n = int(sys.stdin.readline())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 초기 설정, 무한으로 설정
min_cost = float('inf')
dfs(0, {0}, 0)

print(min_cost)