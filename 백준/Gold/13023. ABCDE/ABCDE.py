#13023

import sys

def back(index,arr):
    global check
    if len(arr)==5:
        check=True
        return 
    for i in friend[index]:
        if visited[i]:
            continue
        visited[i]=True
        arr.append(i)
        back(i,arr)
        arr.pop()
        visited[i]=False


m,n=map(int, sys.stdin.readline().split())
friend=[[] for _ in range(m)]
visited=[False]*m

for _ in range(n):
    a,b=map(int, sys.stdin.readline().split())
    friend[a].append(b)
    friend[b].append(a)
check=False
for i in range(m):
    visited[i] = True
    back(i, [i])  # 시작 노드부터 depth=1
    visited[i] = False
    if check:
        break
print(1 if check else 0)