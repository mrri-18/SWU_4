n,m=map(int, input().split())
square=[]

for _ in range(n):
    square.append(input())
step=1
max_meter=0
while step<min(n,m):
    for i in range(n):
        for j in range(m):
            nx=i+step
            ny=j+step
            if 0 <= nx <n and 0 <= ny < m:
                if square[i][j]==square[i][ny]==square[nx][j]==square[nx][ny]:
                    max_meter=step
    step+=1
print((max_meter+1)**2)


