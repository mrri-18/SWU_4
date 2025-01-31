import sys

def back(index,arr):
    if len(arr)==m : # 종료 조건
        print(' '.join(map(str,arr)))
        return
    for i in range(len(index)):
        if visited[i]: # 중복 비허용
            continue
        visited[i]=True
        arr.append(index[i]) 
        back(index,result)
        arr.pop()
        visited[i]=False


n,m=map(int, sys.stdin.readline().split())
result=[]
num= list(map(int,sys.stdin.readline().split()))
num.sort()
visited=[False]*(n+1)
back(num,result)