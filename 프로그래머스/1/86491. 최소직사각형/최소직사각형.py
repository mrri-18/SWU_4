def solution(sizes): 
    width=[]
    height=[]
    
    #그리디
    for i,j in sizes:
        width.append(max(i,j))
        height.append(min(i,j))        
        
    return max(width)*max(height)
    