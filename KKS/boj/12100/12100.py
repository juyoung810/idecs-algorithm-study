from copy import deepcopy

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

def move(board, dir):
    #move to right side
    if dir == 0:
        for i in range(n):
            top = n - 1 #현재 단계에서 고려할 마지막 칸
            for j in range(n-2,-1,-1): #가로기준 마지막 칸 하나 전부터
                if board[i][j]: # 값이 0이 아니면
                    tmp = board[i][j] #일단 현재칸의 값 tmp에 넣고
                    board[i][j] = 0 #현재칸 비워줌
                    if board[i][top] == 0: #옆칸이 비어있으면
                        board[i][top] = tmp #tmp값 넣어줌 -> 즉 그대로 옆으로 이동
                    elif board[i][top] == tmp: #만약에 옆칸이 tmp랑 같으면
                        board[i][top] = tmp *2 #옆칸 값 * 2
                        top -= 1 #그리고 고려해야할 마지막 칸을 한칸 왼쪽으로 이동
                    else: #값이 있긴한데 tmp랑 다를 때
                        top -= 1 #고려해야할 칸 왼쪽으로 한칸 이동하고
                        board[i][top] = tmp #그자리에 tmp넣어줌 사실 원래 값 그대로 있는거랑 같음
    #move to left side
    elif dir == 1:
        for i in range(n):
            top = 0
            for j in range(1, n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][top] == 0:
                        board[i][top] = tmp
                    elif board[i][top] == tmp:
                        board[i][top] = tmp * 2
                        top += 1
                    else:
                        top += 1
                        board[i][top] = tmp

    elif dir == 2:  # 남쪽
        for j in range(n):
            top = n - 1
            for i in range(n - 2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[top][j] == 0:
                        board[top][j] = tmp
                    elif board[top][j] == tmp:
                        board[top][j] = tmp * 2
                        top -= 1
                    else:
                        top -= 1
                        board[top][j] = tmp

    else:
        for j in range(n):
            top = 0
            for i in range(1, n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[top][j] == 0:
                        board[top][j] = tmp
                    elif board[top][j] == tmp:
                        board[top][j] = tmp * 2
                        top += 1
                    else:
                        top += 1
                        board[top][j] = tmp

    return board

def dfs(board, cnt):
    global ans
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                ans = max(ans, board[i][j])
        return

    for i in range(4):
        tmp_board = move(deepcopy(board), i)
        dfs(tmp_board, cnt + 1)

ans = 0
dfs(graph, 0)
print(ans)