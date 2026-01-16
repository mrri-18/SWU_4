def solution(sizes): 
    width=[]
    height=[]
    
    #그리디
    for i,j in sizes:
        width.append(max(i,j)) # 데이터 단순화=> 가로가 긴 쪽으로 고정
        height.append(min(i,j))        
        
    return max(width)*max(height)
    