def solution(sizes): 
    width=[]
    height=[]
    for i,j in sizes:
        if i>j: 
            width.append(i)
            height.append(j)
        else:
            width.append(j)
            height.append(i)
    return max(width)*max(height)