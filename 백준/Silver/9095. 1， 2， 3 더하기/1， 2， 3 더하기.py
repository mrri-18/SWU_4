import sys

count=int(sys.stdin.readline()) # 총 케이스

while count > 0 :
    number=int(sys.stdin.readline())
    answer=0
    # 1, 2, 3 덧셈 계산
    for n1 in range(1,4):
        if n1 == number : answer+=1
        for n2 in range(1,4):
            if (n1+n2) == number : answer+=1
            for n3 in range(1,4):
                if(n1+n2+n3)==number : answer+=1
                for n4 in range(1,4):
                    if (n1+n2+n3+n4)==number : answer+=1
                    for n5 in range(1,4):
                        if(n1+n2+n3+n4+n5)==number : answer+=1
                        for n6 in range(1,4):
                            if(n1+n2+n3+n4+n5+n6)==number: answer+=1
                            for n7 in range(1,4):
                                if(n1+n2+n3+n4+n5+n6+n7)==number: answer+=1
                                for n8 in range(1,4):
                                    if(n1+n2+n3+n4+n5+n6+n7+n8)==number: answer+=1
                                    for n9 in range(1,4):
                                        if(n1+n2+n3+n4+n5+n6+n7+n8+n9)==number: answer+=1
                                        for n0 in range(1,4):
                                            if(n1+n2+n3+n4+n5+n6+n7+n8+n9+n0)==number: answer+=1
    
    print(answer) # 경우의 수 출력
    count-=1
