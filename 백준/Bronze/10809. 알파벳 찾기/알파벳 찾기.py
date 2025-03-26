import sys

word=sys.stdin.readline().strip()
alpha=[-1]*26

for i in range(len(word)):
    if alpha[ord(word[i])-97]==-1:
        alpha[ord(word[i])-97]=i

for i in alpha:
    print(i, end=' ')
