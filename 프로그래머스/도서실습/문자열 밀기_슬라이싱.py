def solution(A, B):
    if A == B : return 0
    for i in range(1,len(A)): 
        tmp=A[-i:]+A[:len(A)-i] 
        if tmp==B: return i
    return -1
