import sys

input=sys.stdin.readline

number=input()
new=sorted(number, reverse=True)
print(''.join(new))
