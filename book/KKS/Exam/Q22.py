from collections import deque

def move(p1, p2, new_board):
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    poss = []
    for dx, dy in dirs:
        pos1 = (p1[0] + dy, p1[1] + dx)
        pos2 = (p2[0] + dy, p2[1] + dx)
        if new_board[pos1[0]][pos1[1]] == 0 and new_board[pos2[0]][pos2[1]] == 0:
            poss.append((pos1, pos2))

    #수평일때 회전 ㅡ -> ㅣ
    if p1[0] == p2[0]:
        for i in [-1,1]: #위로 회전, 아래로 회전
            if new_board[p1[0]+i][p1[1]] == 0 and new_board[p2[0]+i][p2[1]] == 0:
                poss.append((p1, (p1[0] + i, p1[1])))
                poss.append((p2, (p2[0] + i, p2[1])))
    else:
        for i in [-1,1]:
            if new_board[p1[0]][p1[1]+i] == 0 and new_board[p2[0]][p2[1]+i] == 0:
                poss.append(((p1[0], p1[1]+i), p1))
                poss.append(((p2[0], p2[1]+i), p2))
    return poss



def solution(board):
    N = len(board)
    new_board = [[1] * (N+2) for _ in range(N+2)]
    # 태두리 패딩
    for i in range(N):
        for j in range(N):
            new_board[i+1][j+1] = board[i][j]
    q = deque([((1, 1), (1, 2), 0)])
    confirm = {((1, 1), (1, 2))}
    while q:
        p1, p2, time = q.popleft()
        if p1 == (N,N) or p2 == (N,N):
            return time
        for nxt in move(p1,p2, new_board):
            if nxt not in confirm:
                q.append((*nxt, time+1))
                confirm.add(nxt)
