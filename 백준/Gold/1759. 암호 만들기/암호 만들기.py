import sys

def dfs(S, start, arr):
    # 종료 조건
    if len(arr) == l:
        vowels = len(set(arr) & alpha)  # 모음 개수
        consonants = len(arr) - vowels  # 자음 개수
        if vowels >= 1 and consonants >= 2:
            result.append(''.join(arr))
        return

    if start == len(S):  # 탐색이 끝난 경우
        return

    # 현재 알파벳 포함 X
    dfs(S, start + 1, arr)

    # 현재 알파벳 포함 O
    arr.append(S[start])
    dfs(S, start + 1, arr)
    arr.pop()  # 백트래킹

result = []
alpha = {'a', 'e', 'i', 'o', 'u'}  # 모음 집합
l, c = map(int, sys.stdin.readline().split())
array = list(sys.stdin.readline().split())
array.sort()  # 정렬

dfs(array, 0, [])
result.sort()  # 결과 정렬
for i in result:
    print(i)
