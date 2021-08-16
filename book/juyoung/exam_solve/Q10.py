# 열쇠(M)은 항상 자물쇠(N) 보다 작다
# 최대 크기 20 * 20 -> 한번 탐색에 400 연산 필요
# 파이썬은 1초에 2000만번 정도 가능 -> 완전 탐색 가능

# 완전 탐색 위해 자물쇠의 크기를 3배 이상으로 늘리기
# 왼쪽 부터 1 씩 옮기면서 4방향 모두 회전해 보면서, 모든 열쇠 부분의 합이 1되는지 확인

# 시계 방향 90도 돌리는 코드
def rotata_a_matrix_by_90_degree(a):
    n = len(a) # 행 길이 계산
    m = len(a[0]) # 열 길이 계산
    result = [[0] * n for _ in range(m)] # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j] # 행의 길이 -현재 행-1 (0부터 시작이니까) : 1행 -> 마지막 열 되니까
    return result

# 자물쇠의 중간 부분이 모두 1인지 확인하는 코드
def check(new_lock):
    lock_length = len(new_lock) # M 길이 알기 위해
    for i in range(lock_length,lock_length*2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key,lock):
    n = len(lock)
    m = len(key)
    # 자물쇠 크기 기존의 3배로
    new_lock = [[0] * (n*3) for _ in range(n*3) ]
    # 새로운 자물쇠의 중간 부분에 기존 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    # 4가지 방향에 대해 확인하며, 왼쪽으로 1씩 이동
    for rotation in range(4):
        key = rotata_a_matrix_by_90_degree(key) # 열쇠 회전
        # 자물쇠 중심 2배까지만 확인하면 됨
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]

                # 새로운 자물쇠에 열쇠가 정확히 들어 맞는지 검사
                if check(new_lock):
                    return True
                # 자물쇠에서 열쇠 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]

    return False




