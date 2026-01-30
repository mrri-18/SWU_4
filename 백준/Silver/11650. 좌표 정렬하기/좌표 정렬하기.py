import sys

input=sys.stdin.readline

num=int(input())
dim=[]

for i in range(num):
    x,y=map(int,input().split())
    dim.append([x,y])
dim.sort(key=lambda x:(x[0],x[1]))
for x,y in dim:
    print(x, y)