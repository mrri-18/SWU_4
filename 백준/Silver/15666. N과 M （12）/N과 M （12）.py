#15666

import sys

def back(number,arr,index):
    if len(arr)==m : # 종료 조건
        if arr not in answer:
            answer.append(arr[:])
        return        
    for i in range(index,len(number)): # 방문했는지 확인 x
        arr.append(number[i]) 
        back(number,result,i)
        arr.pop()


n,m=map(int, sys.stdin.readline().split())
result=[]
answer=[]
num= list(map(int,sys.stdin.readline().split()))
num.sort()
back(num,result,0)
for i in answer:
    for j in i:
        print(j, end=' ')
    print('')