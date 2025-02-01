import sys

def back(index, add):
    global count  
    if sum(add) == m and len(add) > 0:
        count+=1
    
    for i in range(index,n):
        add.append(num[i])
        back(i+1, add)
        add.pop()

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num.sort()

count = 0  
back(0, [])
print(count)  