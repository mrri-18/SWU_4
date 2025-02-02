#14888 dfs로 풀기
import sys

min_num=10**9+1
max_num=-10**9-1

def dfs(index, total,plus,minus,multi,div):
    global max_num, min_num

    if index==n: # 종료조건
        max_num=max(max_num, total)
        min_num=min(min_num, total)

        return
    
    if plus:
        dfs(index+1, total+array[index], plus-1,minus,multi,div)
    if minus:
        dfs(index+1, total-array[index], plus,minus-1,multi,div)
    if div:
        dfs(index+1, int(total/array[index]), plus,minus,multi,div-1)
    if multi:
        dfs(index+1, total*array[index], plus,minus,multi-1,div)

    

n=int(sys.stdin.readline())
array=list(map(int, sys.stdin.readline().split()))
cal=list(map(int,input().split()))

dfs(1,array[0],cal[0], cal[1], cal[2], cal[3])
print(max_num)
print(min_num)