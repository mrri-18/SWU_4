
import math

def lcm(n,m):
    return n*m//math.gcd(n,m)

def solution(arr):    
    while True:
        arr.append(lcm(arr.pop(), arr.pop()))
        if len(arr)==1:
            return arr[0]