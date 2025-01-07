def solution(numbers, target):
    answer = 0

    def dfs(index, current_sum):
        nonlocal answer
        if index == len(numbers):  # 모든 숫자를 다 사용한 경우 
            if current_sum == target:  
                answer += 1
            return        
        # 현재 숫자를 더하거나 빼는 두 가지 경우=
        dfs(index + 1, current_sum + numbers[index])  
        dfs(index + 1, current_sum - numbers[index])  

    dfs(0, 0)  # 0번 인덱스, 합은 0부터 시작
    return answer
