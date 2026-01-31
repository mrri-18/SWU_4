import sys
input=sys.stdin.readline

num=int(input())

for i in range(num):
    strings=[]
    blank=input().strip()
    for j in blank:
        if j =="(":
            strings.append(j)
        else: 
            if len(strings)==0:
                strings.append(j)
                break
            if strings[-1]=="(": strings.pop()
    if len(strings)==0: print("YES") 
    else: print("NO")
        
    
        
    