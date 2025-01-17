def solution(rsp):
    d = {'0': '5', '2': '0', '5': '2'}
    result = []
    for i in rsp:
        result.append(d[i])  # 변환된 값을 리스트에 추가
    return ''.join(result)   # 리스트를 문자열로 연결
        
        