def solution(babbling):
    answer = 0
    baby=["aya","ye","woo","ma"]
    for i in babbling:
        for j in baby:
            if j*2 not in i:  # 연속해서 같은 발음이 아닌 경우에만 교체
                i=i.replace(j," ")
        if i.isspace():
            answer+=1

        
    return answer
