def hanoi(n, start, end, aux, answer):
    if n == 1:
        answer.append([start, end])
        return
    
    hanoi(n-1, start, aux, end, answer)  # n-1개를 임시 기둥
    answer.append([start, end])          # 가장 큰 원판을 추가
    hanoi(n-1, aux, end, start, answer)  # n-1개를 목표로

def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)
    return answer