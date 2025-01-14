import sys,math
from itertools import combinations

t=int(sys.stdin.readline()) # 총 케이스
for _ in range(t):
    num=list(map(int, sys.stdin.readline().split()))
    num=num[1:] 
    answer=0 # gcd 합 저장
    combi=list(combinations(num,2))
    for i in combi:
        answer+=math.gcd(i[0],i[1])
    print(answer)