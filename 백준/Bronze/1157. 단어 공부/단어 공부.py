word=input().upper()
count=[0]*26
for i in range(len(word)):count[ord(word[i]) - 65]+=1
max=0
max_index=0
k=-1
same=0
while(1):
    k+=1
    if (k == 26 and same==0):
        print(chr(max_index + 65))
        break
    elif(k==26 and same==1):
        print('?')
        break
    if(max<count[k]):
        max=count[k]
        max_index=k
        same=0
    elif(max==count[k] and max!=0): same=1