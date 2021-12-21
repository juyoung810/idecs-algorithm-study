# 감시 피하기


import sys
input = sys.stdin.readline

def see():
    for r,c in t:
        for i in range(4):
            nr = r
            nc = c
            while True:
                nr = nr + dr[i]
                nc = nc + dc[i]
                if 0 <= nr < n and 0 <= nc < n:
                    if board[nr][nc] == "S":
                        return False
                    if board[nr][nc] != "X":
                        break
                else:
                    break
    return True

# 완전 탐색으로 3개의 기둥 설치
def obstacle(cnt,x,y):
    global answer
    if cnt == 3:
        if see() is True:
            answer = "YES"
            return
        # 다 감시 안되는 경우
        return

    for i in range(x,n):
        for j in range(y,n):
            if board[i][j] == "X":
                board[i][j] = "O"
                obstacle(cnt+1,i,j+1)
                if answer == "YES":
                    return
                board[i][j] = "X" # 다시 허물기
        y = 0


# 한 방향으로 dfs 하기
dr = [1,-1,0,0]
dc = [0,0,-1,1]
# 자연수 n 입력받기
n = int(input())
# board
board = []
for _ in range(n):
    board.append(input().split())
# 선생님 좌표 저장
t = []
for i in range(n):
    for j in range(n):
        if board[i][j] == "T":
            t.append([i,j])

answer = "NO"
obstacle(0,0,0)
print(answer)
