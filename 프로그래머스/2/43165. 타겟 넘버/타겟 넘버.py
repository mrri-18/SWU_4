def solution(numbers, target):
    stack=[(0,0)] #curr_sum, idx
    # visited=[False]*(len(numbers)+1)
    answer=0
    
    while stack :
        curr_sum, idx=stack.pop()
        if idx==len(numbers):
            if target==curr_sum:
                answer+=1
            else:
                continue
        # if not visited[idx]:
        #     visited[idx]=True
        else:
            stack.append((curr_sum+numbers[idx],idx+1))
            stack.append((curr_sum-numbers[idx],idx+1))
            


    return answer
