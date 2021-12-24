# boj 10451 : 순열 사이클 by seoyoung
> 문제 주소: https://www.acmicpc.net/problem/10451
>
> silver 2

## 문제
n개의 정수로 이루어진 순열이 주어졌을 때, 순열 사이클의 개수를 구하는 프로그램을 작성하자.

## 문제 해결 방향
사이클이라고 해서 단순이 서로소 집합을 활용한 사이클 판별을 이용하면 될 줄 알았는데, 방향성이 없는 경우에만 사용 가능.\
따라서 DFS를 이용해야 한다.

모든 인덱스에 대해서, 방문 여부를 확인한다. 방문하지 않았으면 다음 노드로 이동해 방문여부를 확인한다.\
이미 방문한 노드에 방문하면 사이클이 있는 것이므로 결과값에 +1을 한다.

## 소스코드
```python
import sys
input = sys.stdin.readline
sys.setrecursionlimit(2000)     # 타임아웃을 막기 위해 최대 재귀를 늘려준다.

def dfs(x):
    visited[x] = True
    num = numbers[x-1]
    if not visited[num]:
        dfs(num)


# 입력 데이터 받기
t = int(input())

for case in range(t):
    n = int(input())
    numbers = list(map(int, input().split()))
    visited = [True] + [False] * n
    cnt = 0

    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
            cnt += 1

    print(cnt)
```
