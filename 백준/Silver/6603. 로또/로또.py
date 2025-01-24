import sys
from itertools import combinations

while True:
    combi=list(map(int, sys.stdin.readline().split()))
    n=combi[0]
    if n == 0:
        break
    combi=combi[1:]

    for i in combinations(combi,6):
        for x in list(i):
            print(x,end=' ')
        print('')
    print(' ')