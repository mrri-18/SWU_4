import sys

def back(number,arr,index):
    if len(arr)==m : # 종료 조건
        print(' '.join(map(str,arr)))
        return
    for i in range(index,len(number)):
        if visited[i]: # 중복 비허용
            continue
        visited[i]=True
        arr.append(number[i]) 
        back(number,result,i+1)
        arr.pop()
        visited[i]=False


n,m=map(int, sys.stdin.readline().split())
result=[]
num= list(map(int,sys.stdin.readline().split()))
num.sort()
visited=[False]*(n+1)
back(num,result,0)