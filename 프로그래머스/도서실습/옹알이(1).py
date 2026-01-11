def solution(babbling):
    answer=[]
    for i in babbling:
        for x in ["aya", "ye","woo","ma"]:
            if x in i: 
                i=i.replace(x," ") # 말할 수 있는 문자열 공백 처리, 빈칸으로 두는 이유는 가운데 문자열을 제거하고 합치는 과정에서 말할 수 있는 단어로 인식할 수 있기 때문
        if not i.isspace(): answer.append(i) # 공백으로 이뤄졌는지 확인
    return len(babbling)-len(answer)
