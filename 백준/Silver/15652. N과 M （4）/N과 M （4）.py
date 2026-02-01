import sys
input=sys.stdin.readline

n,m=map(int,input().split())

def back(combi,num):
    if len(combi)==m:
        print(*combi)
        return
    else:
        for i in range(num,n+1): 
            combi.append(i)
            back(combi,i)
            combi.pop()

back([],1)