import sys

input=sys.stdin.readline

num=int(input())
dim=[]

for i in range(num):
    x,y=map(int,input().split())
    dim.append([x,y])
dim.sort(key=lambda x:(x[1],x[0]))
for x,y in dim:
    print(x, y)