def solution(sizes): 
    width=[]
    height=[]
    for i,j in sizes:
        if i<j: # 세로가 더 긴 경우
            i,j=j,i
        width.append(j)
        height.append(i)
    return max(width)*max(height)