import sys
input=sys.stdin.readline

n,m=map(int,input().split())
visited=[False]*(n+1)

def back(combi,num):
    if len(combi)==m:
        print(*combi)
        return
    else:
        for i in range(num,n+1):
            if visited[i]:
                continue
            else:
                combi.append(i)
                visited[i]=True
                back(combi,i+1)
                combi.pop()
                visited[i]=False # 다시 방문 가능

back([],1)