def solution(arr):
    answer=[arr[0]]
    for i in arr: 
        if i==answer[-1]: # 연속적으로 같은 숫자인 경우 
            pass
        else: # 다른 숫자가 오는 경우
            answer.append(i)
    return answer
        