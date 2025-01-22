import sys
from itertools import permutations

def calculate(a): # 합을 계산해서 리턴
    result=0
    for x in range(len(a)-1):
        result=result+abs(a[x]-a[x+1])
    return result

n=int(sys.stdin.readline())
array=list(map(int, sys.stdin.readline().split()))
answer=[]
for i in permutations(array,n):
    answer.append(calculate(i))

print(max(answer))