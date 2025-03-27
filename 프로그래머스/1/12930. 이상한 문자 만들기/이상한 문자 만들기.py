def solution(s):
    answer=[]
    for word in s.split(" "):
        word=list(word) # 각 문자를 바꾸기 위해 리스트로 변환
        for index, char in enumerate(word):
            if index%2==0:
                word[index]=char.upper()
            else:
                word[index]=char.lower()
        answer.append(''.join(word))
    
    return ' '.join(answer)