n=int(input())
answer=list(map(int,input().split()))
count=0
for num in answer:
    if num==1:
        count+=1
        continue
    for i in range(2,num):
        if(num%i!=0):
            continue
        else: #소수가 아닌 경우
            count+=1
            break
print(len(answer)-count) #소수인 경우 print