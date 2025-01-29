def solution(brown, yellow):
    for i in range(brown,0,-1):
        height=(brown-(i*2))/2
        if i*(height+2) -yellow==brown:
            return [max(i,height+2), min(i,height+2)]
        