import sys
input = sys.stdin.readline

#계수정렬 활용
n = int(input())
arr = [0] * (10000 + 1) # 입력값 10000개

#각 입력값에 해당하는 인덱스의 값 증가
for _ in range(n):
    arr[int(input())] += 1
  
#arr에 기록된 정보 확인
for i in range(len(arr)):
    if arr[i] != 0: # 입력받은 데이터들을 출력
        for _ in range(arr[i]):
            print(i)
