'''
< 자물쇠와 열쇠 >
자물쇠에는 홈이 파여 있고 열쇠 또한 홈과 돌기 부분이 있다. 열쇠는 회전과 이동이 가능.
열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열리게 되는 구조.
자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠에 영향 X
자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 함. 돌기끼리 만나면 안됨
자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠 열 수 있음

열쇠를 나타내는 2차원 배열 key와 자물쇠를 나타내는 2차원 배열 lock이 매개변수로 주어질 때,
열 수 있으면 true,  없으면 false를 return 라도록 solution 함수 완성

입출력 예
key [[0,0,0],[1,0,0],[0,1,1,]]
lock [[1,1,1],[1,1,0],[1,0,1]]
result  true
'''

# 열쇠 넣기(패딩한 가운데에)
def attach(x, y, m, key, board):
    for i in range(m):
        for j in range(m):
            board[x+i][y+j] += key[i][j]


# 2차원 리스트 90도 회전
def rotate(arr):
    return list(zip(*arr[::-1]))

# 자물쇠의 중간 부분이 모두 1인지 확인
def check(board, m, n):
    for i in range(n):
        for i in range(n):
            if board[m+i][m+j] != 1:
                return False
    return True

# 열쇠 빼기(1 아니면)
def detach(x, y, m, key, board):
    for i in range(m):
        for j in range(m):
            board[x+i][y+j] -= key[i][j]

# solution. m : key, n : lock
def solution(key, lock):
    m, n = len(key), len(lock)
    # 패딩
    board = [[0] * (m*2+n) for _ in range(m*2+n)]
    # 자물쇠를 중앙에 배치
    for i in range(n):
        for j in range(n):
            board[m + i][m + j] = lock[i][j]

    # 4가지 방향에 대해 반복
    rotated_key = key
    for _ in range(4):
        rotated_key = rotate(rotated_key)
        for x in range(1, m+n):
            for y in range(1, m+n):
                # 열쇠 넣어보기
                attach(x, y, m, rotated_key, board)
                if (check(board, m, n)):
                    return True
                detach(x, y, m, key, board)
    return False