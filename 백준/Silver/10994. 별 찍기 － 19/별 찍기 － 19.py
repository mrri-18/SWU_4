import sys
def draw_star(n):
    size = 4 * n - 3
    board = [[' ' for _ in range(size)] for _ in range(size)]

    def draw_layer(x, y, current_size):
        if current_size == 1:  # 종료 조건
            board[x][y] = '*'
            return
        length = 4 * current_size - 3  # 현재 한 변의 길이
        # 가장 바깥
        for i in range(length):
            board[x][y + i] = '*'  # 상
            board[x + length - 1][y + i] = '*'  # 하
            board[x + i][y] = '*'  # 좌
            board[x + i][y + length - 1] = '*'  # 우

        draw_layer(x + 2, y + 2, current_size - 1)

    draw_layer(0, 0, n)
    return board


def print_star(board):
    for row in board:
        print(''.join(row))

n = int(sys.stdin.readline())
result = draw_star(n)
print_star(result)