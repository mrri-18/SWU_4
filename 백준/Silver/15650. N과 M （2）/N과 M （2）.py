#15650
import sys

def back(index,arr):
    if len(arr)==m: # 종료 조건
        print(' '.join(map(str,arr)))
        return
    for i in range(index,n+1):
        if visited[i]:
            continue
        visited[i]=True
        arr.append(i) # 가지치기
        back(i+1,arr) # 현재 선택한 숫자 i를 기준으로 다음 탐색 범위를 제한
        arr.pop()
        visited[i]=False

n,m=map(int, sys.stdin.readline().split())
result=[]
visited=[False]*(n+1)
back(1,result)
