import sys

input=sys.stdin.readline

num=int(input())
words=[]

for i in range(num):
    words.append(input().strip())

wordset=sorted(set(words), key=lambda x: (len(x), x))
 
for x in wordset:
    print(x)