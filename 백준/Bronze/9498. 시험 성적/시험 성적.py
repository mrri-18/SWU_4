import sys

score=int(sys.stdin.readline())
if score>89:
    print("A")
elif score>79:
    print("B")
elif score>69:
    print("C")
elif score>59:
    print("D")
else:
    print("F")