def attach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x + i][y + j] += key[i][j]


def detach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x + i][y + j] -= key[i][j]


def check(board, M, N):
    for i in range(N):
        for j in range(N):
            if board[M + i][M + j] != 1:
                return False
    return True


def rotate90(arr):
    return list(zip(*arr[::-1]))
# M:열쇠, N:자물쇠
def solution(key, lock):
    M, N = len(key), len(lock)  # 문제의 논리에 따라 진행하다
    #패딩
    board = [[0] * (M * 2 + N) for _ in range(M * 2 + N)]
    # 자물쇠를 중앙에 배치
    for i in range(N):
        for j in range(N):
            board[M + i][M + j] = lock[i][j]

    rotated_key = key
    # 모든 방향 (4번 루프)
    for _ in range(4):
        rotated_key = rotate90(rotated_key)
        for x in range(1, M + N):
            for y in range(1, M + N):
                # 열쇠 넣어보기
                attach(x, y, M, rotated_key, board)
                if (check(board, M, N)):
                    return True
                detach(x, y, M, rotated_key, board)
    return False