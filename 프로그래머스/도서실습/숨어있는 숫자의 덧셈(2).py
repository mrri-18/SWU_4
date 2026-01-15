def solution(my_string):
    for i in my_string:
        if i.isalpha(): my_string=my_string.replace(i," ")
    return sum(list(map(int, my_string.split()))) # 문자를 공백처리해서 숫자만 더하는 코드


#     answer=[] 숫자만 추출해서 저장하는 방식, 오히려 list로 바꾸니까 문자를 처리하기 어려웠음
#     number=""
#     num=0
#     for i in my_string:
#         if i.isalpha():
#             if len(number)!=0:
#                 answer.append(number)
#                 number=""
#         elif i.isdigit():
#             number+=i
#     print(answer)
#     return sum(list(map(int, answer)))
    
