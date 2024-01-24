import sys

s=[]
num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for i in range(int(input())):
    cmd,*x = sys.stdin.readline().split()
    if x:
        x1=int(x[0])
        if (cmd == "add"):
            if x1 not in s:
                s.append(x1)
        elif (cmd == "remove"):
            if x1 in s:
                s.remove(x1)
            # print(s)
        elif (cmd == "check"):
            if x1 in s:
                print(1)
                # print(s)
            else:
                print(0)
        elif (cmd == "toggle"):
            if x1 not in s:
                s.append(x1)
            elif x1 in s:
                s.remove(x1)
    else:
        if(cmd == "all"):
            s.clear()
            s.extend(num)
        elif (cmd == 'empty'):
            s.clear()
