import sys

def back(number,arr):
    if len(arr)==m : # 종료 조건
        print(' '.join(map(str,arr)))
        return
    for i in range(len(number)):
        visited[i]=True
        arr.append(number[i]) 
        back(number,result)
        arr.pop()
        visited[i]=False


n,m=map(int, sys.stdin.readline().split())
result=[]
num= list(map(int,sys.stdin.readline().split()))
num.sort()
visited=[False]*(n+1)
back(num,result)