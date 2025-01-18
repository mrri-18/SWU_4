import sys

binary=sys.stdin.readline()
binary=int(binary,2)
print(oct(binary)[2:])