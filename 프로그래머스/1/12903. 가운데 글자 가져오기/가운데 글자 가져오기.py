def solution(s):
    if len(s)%2==0:
        index=int(len(s)/2-1)
        return s[index:index+2]
    else:
        index=len(s)//2
        return s[index]