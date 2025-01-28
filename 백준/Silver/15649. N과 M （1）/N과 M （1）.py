import sys

def back(index,arr):
    if len(arr)==m: # 종료 조건
        print(' '.join(map(str,arr)))
        return
    for i in range(1,n+1):
        if visited[i]:
            continue
        visited[i]=True
        arr.append(i)
        back(index+1,result)
        arr.pop()
        visited[i]=False


n,m=map(int, sys.stdin.readline().split())
result=[]
visited=[False]*(n+1)
back(1,result)