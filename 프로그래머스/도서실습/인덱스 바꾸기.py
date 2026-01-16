def solution(my_string, num1, num2):
    my_string=list(my_string) # 문자열 자체의 원소를 바꿀 수 없기 때문에 리스트 변환
    tmp=my_string[num1]
    my_string[num1]=my_string[num2]
    my_string[num2]=tmp
    return ''.join(my_string)
