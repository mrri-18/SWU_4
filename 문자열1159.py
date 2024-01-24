N=int(input())
alp=[0]*26
for i in range(N):
    name=input()
    alp[ord(name[0])-97]+=1
if(max(alp)<5):
    print("PREDAJA")
for i in range(len(alp)):
    if alp[i]>=5:
        print(chr(i+97),end='')