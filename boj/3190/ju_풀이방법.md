### boj 3190: 뱀
> 문제 주소: https://www.acmicpc.net/problem/3190

#### 문제 해결 방법
##### 구현은 모든 문제 조건을 세세하게 만족시키는 것이 중요하다.
- 뱀의 머리를 추적한다.
- 뱀이 사과를 먹으면 몸 길이나 늘어나고, 유지 된다.
  
         # 벽과 부딪히면 종료
        if nc < 0 or nc >= N or nl < 0 or nl >= N:
            state = False
            break
        # 자기 자신의 몸과 부딪히면 종료
        elif [nl, nc] in bam:
            state = False
            break

- 뱀이 직선으로 움직이는 것이 아니므로 , 뱀의 머리의 좌표를 큐에 저장하고, 사과를 먹지 않았을 시 앞에서 부터 pop해서 꼬리를 처리해준다
- ** 뱀이 사과를 먹었을 시 해당 사과를 지워준다.
  
        # 머리 먼저 이동
        head[0] = nl
        head[1] = nc
        bam.append([nl,nc])
        # 사과 존재하지 않으면 꼬리 움직인다.
        if board[nl][nc] == 0:
            bam.pop(0)
        # 사과가 존재하는 경우 해당 사과 지운다
        else:
            board[nl][nc] = 0
  

-  방향을 저장하고, 하나씩 pop 한다. 모든 방향 지시가 끝 날 경우 가장 큰 수와 , 없는 방향을 지정해 계속 한 뱡향으로 나갈 수 있도록 한다.
       
        while state:
        if len(directions) != 0 :
            direction = directions.pop(0)
        else:
            direction[0] = str(N*N)
            direction[1] = "T"
        while time_count < int(direction[0]):
             time_count += 1
            # 시작 오른쪽  = 동쪽
            nl = head[0] + dl[d]
            nc = head[1] + dc[d]
   
- (북 동 남 서 ) 순서로 dl,dc를 저장하고, 오른쪽 90 회전은 시계 방향, 왼쪽 90은 반시계 방향으로 방향을 이동할 수 있도록 한다.
지정된 방향지시가 없는 경우 방향 변화하지 않는다.
  

        if direction[1] == 'D':
        d = (d + 1) % 4
         elif direction[1] == 'L':
        d = (d - 1 + 4) % 4
        else: continue





##### 참고.. 
        
        bam = [head]
        while True:
            head = [1,2]
            bam.append[head]

 이렇게 할 경우 head는 배열이므로 주소가 같으므로, 값이 변동이 동시에 일어나서 bam = [[1,2],[1,2]]가 되므로 주의 하자
