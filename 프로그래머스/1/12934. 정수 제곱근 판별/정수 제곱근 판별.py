import math

def solution(n):
    if math.sqrt(n)%1==0: # 제곱이라면
        return (math.sqrt(n)+1)**2
    else:
        return -1