import sys

def back(index, add):
    global max_income  
    if index<=n:
        if max_income<sum(add):
            max_income=sum(add)

    if index>=n:
        return
    
    for i in range(index,n):
        if visited[i]: # 중복 비허용
            continue
        visited[i]=True
        add.append(work[i][1])
        back(i+work[i][0], add)
        add.pop()
        visited[i]=False
n=int(sys.stdin.readline())
work = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

max_income = 0  
visited=[False]*(n+1)
back(0, []) # 날짜, (소득)
print(max_income)  

