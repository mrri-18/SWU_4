import sys

def back(number, arr, index):
    if len(arr) == m:
        answer.add(tuple(arr))  # 중복 제거
        return

    for i in range(index, len(number)):  # 중복 선택 가능하므로 인덱스부터 시작
        arr.append(number[i])
        back(number, arr, i)  
        arr.pop()

n, m = map(int, sys.stdin.readline().split())
num = sorted(map(int, sys.stdin.readline().split()))  
answer = set()  

back(num, [], 0)

for seq in sorted(answer):  # 사전순 출력
    print(*seq)
