import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
    _x = [0, 0, 1, -1]
    _y = [1, -1, 0, 0]
    for i in range(4):
        m_x = x+_x[i]
        m_y = y+_y[i]
        if (0<=m_x and m_x <M) and (0<=m_y and m_y<N) and mat[m_x][m_y] ==1:
            mat[m_x][m_y] =0
            dfs(m_x, m_y)
num_list = []
T = int(input())
for _i in range(T):
    M, N, K = map(int, input().split())
    mat = [[0]*N for _j in range(M)]
    num = 0
    for _i in range(K):
        x, y = map(int, input().split())
        mat[x][y] = 1
    for i in range(M):
        for j in range(N):
            if mat[i][j] == 1:
                dfs(i, j)
                num +=1
    num_list.append(num)
for _i in range(T):
    print(num_list[_i])


###############################
# 출처: https://fullmoon1344.tistory.com/85 [태야]

import sys 
sys.setrecursionlimit(10000) 
def dfs(x, y): 
    dx = [1, -1, 0, 0] 
    dy = [0, 0, 1, -1] 
    
    # 상,하,좌,우 확인 
    for i in range(4): 
        nx = x + dx[i] 
        ny = y + dy[i] 
        
        if (0 <= nx < N) and (0 <= ny < M): 
            if matrix[nx][ny] == 1: 
                matrix[nx][ny] = -1
                dfs(nx, ny) 
T = int(input()) 
for _ in range(T): 
    M, N, K = map(int, input().split()) 
    matrix = [[0]*M for _ in range(N)] 
    cnt = 0 
    # 행렬 생성 
    for _ in range(K): 
        m, n = map(int, input().split()) 
        matrix[n][m] = 1 
    for i in range(N): # 행 (바깥 리스트) 
        for j in range(M): # 열 (내부 리스트) 
            if matrix[i][j] > 0: 
                dfs(i, j) 
                cnt += 1 
print(cnt)

