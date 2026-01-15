def solution(arr):
    answer=[arr[0]]
    for i in arr:
        if i==answer[-1]: 
            pass
        else:
            answer.append(i)
    return answer
        