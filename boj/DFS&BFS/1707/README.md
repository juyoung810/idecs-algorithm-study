# boj 1707 : 이분 그래프 by juyoung
> 문제 주소: https://www.acmicpc.net/problem/1707
> 
> gold 4

## 문제 해결 방향
1. BFS로 한 node의 인접한 node의 전체를 둘러보고, 해당 node의 인접 node의 level를 원래 node의 level +1 로 설정한다.
#####   2. node를 pop 해서 인접 리스트에서 인접 node를 찾아서 level를 확인하는데 인접 노드의 level이 pop 한 원래의 node의 level과 같다면, 두 집합으로 나눌 수 없다는 것을 알 수 있다.
```python
def BFS(start):
    visited[start] = 1
    q = deque()
    q.append(start)
    # 인접 노드 찾는다.
    while q:
        be = q.popleft()
        for i in graph[be]:
            # 삼각형(cycle)이 생성되는 지 확인
            if visited[i] == visited[be]:
                return False
            # 한번도 visited 되지 않았을 경우 queue에 삽입
            elif visited[i] == 0:
                visited[i] = visited[be] + 1
                q.append(i)
    bfs 종료
    return True
```
3. connected Graph가 아닐 수 있으니 ,아직 이분이 가능하다면, 다음 BFS 를 시작할 node를 찾는다.
```python
    isCon = True
    for i in range(1, N+1):
        if visited[i] == 0:
            if not BFS(i):
                stdout.write("NO"+'\n')
                isCon = False
                break
    if isCon:
        stdout.write("YES"+'\n')
```
