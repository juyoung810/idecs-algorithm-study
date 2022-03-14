import sys
input = sys.stdin.readline

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]

case = [[0]*N for _ in range(N)]
case[0][0] =1

for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1:
            break
        n, m =case[i][j], mat[i][j] 
        if n >=1:
            if i+m <= N-1:
                case[i+m][j] += n
            if j+m <= N-1:
                case[i][j+m] += n
print(case[N-1][N-1])