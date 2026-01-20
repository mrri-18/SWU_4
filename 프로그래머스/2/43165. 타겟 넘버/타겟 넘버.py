def solution(numbers, target):
    num=[(0,0)]
    answer=0
    while num:
        cur_sum,idx=num.pop()
        if idx==len(numbers) and cur_sum==target:
            answer+=1
        elif idx < len(numbers):
            num.append((cur_sum+numbers[idx], idx+1))
            num.append((cur_sum-numbers[idx], idx+1))
        
    return answer