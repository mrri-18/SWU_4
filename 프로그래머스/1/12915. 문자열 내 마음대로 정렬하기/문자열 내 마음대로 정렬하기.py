def solution(strings, n):
    answer = sorted(strings, key=lambda x: (x[n], x)) # n번째 문자, 문자열 전체를 두고 기준 
    return answer