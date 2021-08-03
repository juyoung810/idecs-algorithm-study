# boj 1520 : 내리막길 by KKS
> 문제 주소: https://www.acmicpc.net/problem/1520
> 
> 난이도: gold 4

## 1.문제설명
![img_2.png](img_2.png)

## 2.문제해결 아이디어.
- 2차원 그리드를 생각해보자
- dfs 이용해서 재귀 개념 이용

## 3.문제접근법
- 그리드에는 경로의 수를 저장함
- 2차원 그리드에서 가보지않은 곳을 전부 -1로 바꿈
- 좌표가(0,0)이 아닌데 가보지 않았으면 0으로 바꿔주고 거기서 상하좌우를 움직임
- 새로운좌표의 값이 현재좌표값보다 더 크면 새로운 좌표에대해 dfs함수 실행
- (0,0)인 좌표 도달하면 1 리턴 (기본단계)
```python
def dfs(x,y):
    #기본조건
    if x == 0 and y == 0:
        return 1
    #해당 좌표의 그리드 값이 -1이면(안가본곳이면)
    if dp[x][y] == -1:
        dp[x][y] = 0 # 0으로 바꿔줌
        for i in range(4): #상하좌우 이동
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and  0 <= ny < m:
                #새로운 좌표의 값이 나보다 커야됨 작은값으로만 이동하니깐
                if graph[x][y] < graph[nx][ny]: 
                    dp[x][y] += dfs(nx, ny) #재귀

    return dp[x][y]
```
## 4.특별히 참고할 사항
- setrecursionlimit으로 재귀 한계를 재설정해줘야함

## 5.코드구현
``` python
import sys
sys.setrecursionlimit(10**8)
#n:세로, m:가로
n, m = map(int,input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

dp = [[-1] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x,y):
    if x == 0 and y == 0:
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and  0 <= ny < m:
                if graph[x][y] < graph[nx][ny]:
                    dp[x][y] += dfs(nx, ny)

    return dp[x][y]

print(dfs(n-1,m-1))
```