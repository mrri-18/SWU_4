n=int(input())
p=list(map(int,input().split()))
count=0
p=sorted(p)
for i in range(1,n+1):
    count=count+p[n-i]*i
print(count)
