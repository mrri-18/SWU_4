def solution(numbers, target):
    stack=[(0,0)] #curr_sum, idx
    answer=0
    
    while stack : 
        curr_sum, idx=stack.pop()
        if idx==len(numbers):
            if target==curr_sum:
                answer+=1
            else:
                continue
        else:
            stack.append((curr_sum+numbers[idx],idx+1))
            stack.append((curr_sum-numbers[idx],idx+1))
            
    return answer
