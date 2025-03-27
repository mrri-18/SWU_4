import sys

for i in range(int(input())):
    repeat, word=sys.stdin.readline().split()
    answer=''
    for j in word:
        answer+=(j*int(repeat))
    print(answer)

