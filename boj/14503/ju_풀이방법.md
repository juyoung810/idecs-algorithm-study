### boj 14503: 로봇 청소기
> 문제 주소: https://www.acmicpc.net/problem/14503


#### 문제 해결 방법
-  2차원 배열로 입력 받기

        board = []
        for i in range(N):
            board.append([int(x) for x in input().split()])

- 왼쪽 방향으로 회전, 4회 회전 했을 경우 원래 방향으로 돌아오므로 후진 해야한다.
후진할 때 방향은 바뀌지 않으므로 변화량 그대로 빼준다.
  
- 후진할 때 후진하는 방향이 벽이면 중단한다.
  
            while True:
            # 왼쪽 방향 회전
            direction = (direction - 1 + 4) % 4
            nr = r + dr[direction]
            nc = c + dc[direction]
            ....
            # 4번 회전했을 때
            if turn_count == 4:
                # 후진
                nr = r - dr[direction]
                nc = c - dc[direction]
                if board[nr][nc] == 0:
                    r = nr
                    c = nc
                else:
                    break
                turn_count = 0

- 청소하는 경우에 해당하지 않으면 turn_count를 증가 시켜준다.

         # 회전한 뱡향이 방이고, 청소 안했을 경우
            if board[nr][nc] == 0 and state[nr][nc] == 0:
                r = nr
                c = nc
                state[r][c] = 1
                room_count += 1
                turn_count = 0
            else:
                turn_count += 1


- 후진 조건을 마지막에 두어 count = 4 가 되는 것을 고려해야한다.