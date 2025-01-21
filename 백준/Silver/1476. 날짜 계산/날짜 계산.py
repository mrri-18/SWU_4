import sys

e,s,m=map(int, sys.stdin.readline().split())
earth=1
sun=1
moon=1
year=1

while(True):
    if earth==e and sun==s and moon==m:
        print(year)
        break
    earth=15 if earth == 14 else (earth+1)%15
    sun=28 if sun == 27 else (sun+1)%28
    moon=19 if moon == 18 else (moon+1)%19
    year+=1