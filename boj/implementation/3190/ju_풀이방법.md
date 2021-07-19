### boj 3190: 뱀
> 문제 주소: https://www.acmicpc.net/problem/3190

#### 문제 해결 방법
##### 구현은 모든 문제 조건을 세세하게 만족시키는 것이 중요하다.
1.  기본 board 만들기
    - N*N 크기의 보드를 만들어 0으로 초기화한다.
    - 사과의 위치를 입력 받아 보드의 해당 위치를 1로 초기화

    ```java
    # 보드의 크기 N*N
    N = int(input())
    board = [[0] * N for _ in range(N)]

    # 사과 위치
    for _ in range((int(input()))):
        r,c = map(int, input().split())
        # 0행 부터 시작 설정 # 행 열
        board[r - 1 ][c - 1] = 1
    ```
2. 이동 조건 만족 시키기
    - 오른쪽으로 이동 시키면 +1, 왼쪽으로 이동 시키면 방향이 -1 이 되도록 dc, dr 리스트를 만들어 변화량을 저장한다.
    - 이동 위치를 받아 저장한다.
    - 받은 이동 위치를 pop 하며 조건에 맞는 시간 동안 해당 뱡향으로 이동 시킨다.
    - 받은 이동 위치만큼 모두 회전한 경우, 마지막 방향으로 나가도록 한다.
    - time_count 변수를 사용해서 , 주어진 시간이 지난 후 방향을 변경하도록 한다.

    ```java
    # 북 동 남 서
    # x : 행
    # y : 열
    dc = [0, 1, 0, -1]
    dr = [-1, 0, 1, 0]

    directions = []
    # 이동 위치 받기
    for _ in range((int(input()))):
        directions.append(list(input().split()))
    con = 0
    # 동쪽(오른쪽 부터 시작)
    d = 1
    while state:
        if len(directions) != 0 :
            direction = directions.pop(0)
        else:
            direction[0] = str(N*N)
            direction[1] = "T"
        while time_count < int(direction[0]):
            time_count += 1
            # 시작 오른쪽  = 동쪽
            nr = head[0] + dr[d]
            nc = head[1] + dc[d]
    			
    			#### 종료 조건 #####
    		if direction[1] == 'D':
    		        d = (d + 1) % 4
    		    elif direction[1] == 'L':
    		        d = (d - 1 + 4) % 4
    		    else: continue
    		    #print(d)
    	

    print(time_count)
    ```
3. 뱀의 길이 조건 만족시키기
- 뱀이 사과를 먹으면 몸의 길이가 늘어나고, 늘어난 길이는 유지된다.
- 뱀이 직선으로 움직이는 것이 아니다. → 뱀의 머리또는 꼬리만을 추적하는 것이 아니라 몸 전체의 좌표를 추적할 수 있도록 해야한다.
- 뱀의 머리가 먼저 움직이고, 사과의 유무에 따라 뱀의 꼬리가 따라온다→ Queue 자료 구조를 이용해서, 머리가 움직일때 마다 좌표를 push하고, 꼬리를 pop 한다.
- 사과가 존재하는 경우 해당 사과를 지워서, 해당 좌표를 재방문 했을 때, 몸의 길이가 또 늘어나지 않도록 한다.

```java
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
```

4. 종료 조건 만족시키기
- 뱀이 벽또는 자신의 몸과 부딪히면 종료된다 → 뱀의 몸의 좌표를 추적해야한다
- while 문을 종료시키기 위해 종료된 경우 state 변수를 false로 만든다.

```java
# 벽과 부딪히면 종료
        if nc < 0 or nc >= N or nr < 0 or nr >= N:
            state = False
            break
        # 자기 자신의 몸과 부딪히면 종료
        elif [nr, nc] in bam:
            state = False
            break
```
##### 참고.. 
        
        bam = [head]
        while True:
            head = [1,2]
            bam.append[head]

 이렇게 할 경우 head는 배열이므로 주소가 같으므로, 값이 변동이 동시에 일어나서 bam = [[1,2],[1,2]]가 되므로 주의 하자
