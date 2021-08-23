'''
< 블록 이동하기 >

준비 중인 로봇은 2X1 크기의 로봇.
0과 1로 이루어진 nXn 크기의 지도에서 2x1 크기의 로봇을 움직여 (n,n) 위치까지 이동할 수 있도록 프로그래밍을 하려고 한다.
로봇이 ㅇ동하는 지도는 가장 왼쪽, 상단의 좌표를 (1,1)로 하여 지도 내에 표시된 숫자 0은 빈칸을, 1은 벽을 나타낸다.
로봇은 벽이 있는 칸 또는 지도 밖으로 이동 불가, 처음에 (1,1) 위치에서 가로 방향으로 놓여 있는 상태로 시작

< 문제 해결 방향 >
bfs로 푼다.
벽을 만나면 회전이 가능한지 여부에 따라 회전시키고 이동?
탐색을 통해 회전이 가능한 경우를 저장한다.
회전하는 경우 가로방향일때는 위/아래에 1이 하나라도 있으면 해당 방향 회전이 불가능
세로방향일때는 왼쪽/오른쪽에 1이 하나라도 있으면 해당 방향 회전이 불가능하다는 것을 이용하여 푼다.

- (1,1) 위치의 로봇을 (n,n)으로 옮기는 최단 거리를 계산하는 문제.
- 로봇의 상태가 두칸 -> 위치정보를 튜플로 처리한다. 집합 자료형을 이용해 관리하면, 한번 방문한 곳은 방문하지 않는다.
- 이동 : 단순히 상, 하, 좌, 우로 이동하는 모든 경우를 계산하면 된다.
- 회전 : 로봇의 가로, 세로 상태까지 고려해야 한다.
    1) 가로상태에서 아래쪽으로 회전 : 아래쪽에 벽이 없어야 한다. 아래 두 칸에 1이 있으면 안된다.
    2) 가로상태에서 위로 회전 : 위쪽에 벽이 없어야 한다. 위 두 칸에 1이 있으면 안된다.
    3) 세로상태에서 오른쪽 회전 : 오른쪽에 벽이 없어야 한다. 오른쪽 두 칸에 1 없음
    4) 세로상태 왼쪽 회전 : 왼쪽 두 칸에 1 없음
- 소스코드의 간단한 작성을 위해 초기에 주어진 맵을 변형하여 외곽에 벽을 둔다.
'''

# 특정한 위치에서 이동 가능한 다음 위치를 반환하는 별도의 get_next_pos() 함수를 구현한다.

from collections import deque

def get_next_pos(pos, board):
    next_pos = []   # 반환 결과(이동 가능한 위치들)
    pos = list(pos) # 현재 위치 정보를 리스트로 변환(집합 -> 리스트)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    # (상, 하, 좌, 우)로 이동하는 경우에 대해서 처리
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]
        # 이동하고자 하는 두 칸이 모두 비어 있다면
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})   # 이동 가능한 위치에 추가

    # 현재 로봇이 가로로 놓여 있는 경우
    if pos1_x == pos2_x:
        for i in [-1, 1]    # 위, 아래로 회전
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:   # 위쪽 혹은 아래쪽 두 칸이 모두 비어있다면
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})

    # 현재 로봇이 세로로 놓여 있는 경우
    elif pos1_y == pos2_y:
        for i in [-1, 1]    # 왼쪽, 오른쪽으로 회전
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0:   # 왼쪽 혹은 오른쪽 두 칸이 모두 비어있다면
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})

    # 현재 위치에서 이동할 수 있는 위치를 반환
    return next_pos

def solution(board):
    # 맵의 외곽에 벽을 두는 형태로 맵 변형
    n = len(board)
    new_board = [[1] * (n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]
    # 너비 우선 탐색(BFS) 수행
    q = deque()
    visited = []
    pos = {(1,1), (1,2)}    # 시작 위치 설정
    q.append((pos, 0))  # 큐에 삽입한 뒤에
    visited.append(pos) # 방문 처리
    # 큐가 빌 때까지 반복
    while q:
        pos, cost = q.popleft()
        # (n, n) 위치에 로봇이 도달했다면, 최단 거리이므로 반환
        if (n, n) in pos:
            return cost
        # 현재 위치에서 이동할 수 있는 위치 확인
        for next_pos in get_next_pos(pos, new_board):
            # 아직 방문하지 않은 위치라면 큐에 삽입하고 방문 처리
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0