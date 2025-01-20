import sys

def dfs(index, current_dwarfs):
    # 종료 조건
    if len(current_dwarfs) == 7:
        if sum(current_dwarfs) == 100:
            current_dwarfs.sort()
            for dwarf in current_dwarfs:
                print(dwarf)
            sys.exit()  # 정답을 찾았으므로 종료
        return

    # 탐색 종료 조건: 더 이상 선택할 난쟁이가 없는 경우
    if index == 9:
        return

    # 분기
    dfs(index + 1, current_dwarfs + [length[index]])

    dfs(index + 1, current_dwarfs)

length = [int(sys.stdin.readline()) for _ in range(9)]

dfs(0, [])