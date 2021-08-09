# boj 11403 : 경로 찾기 by juyoung
> 문제 주소: https://www.acmicpc.net/problem/11403
>
<<<<<<< HEAD
> silver 1
=======
> silver 1

## 문제 해결 방향

- 처음에는 그냥 플루이드 워샬 알고리즘 적용 문제 인 줄 알았다. 그러나, 00: 0->1->2->0 식으로 처리하는 것이 필요했다.
- 최단 경로를 묻는 것이 아니라 __경로의 유무__ 를 묻는 것이다.
- 플루이드 워샬 알고리즘을 수행하며, 기존에 존재하는 경로가 없을 경우 [a][k] VS [k][b] 를 비교해서 
  두 개 모두 0 이 아닌 경우 a->b 경로가 존재한다.
  
### 소스 코드
1. n 을 입력 받아, 경로를 저장하기 위해 n * n 배열을 생성한다
인접 행렬로 주어지기 때문에, 그대로 graph 에 저장한다.
```python
import sys
INF = int(1e9)
input = sys.stdin.readline

n = int(input())

#최단 경로 담는 graph
graph = []
# 인접행렬 입력 받기
for i in range(n):
    graph.append(list(map(int,input().split())))
```

2. 플루이드 워샬 알고리즘을 수행하며, 기존에 경로가 존재하지 않는 경우 
min 함수를 통해 둘 중 하나라도 0 이 존재하면 0이 되도록 한다.
   
```python
# 플루이드 워샬
for k in range(n):
    for a in range(n):
        for b in range(n):
            # 경로가 존재하지 않는다면
            if graph[a][b] != 1:
                # 둘 중 하나라도 0 이 아니면 0 이상이 될 것
                graph[a][b] = min(graph[a][k],graph[k][b])


```
3. 반복문을 통해 graph가 0 이 아닐 경우 1 , 0인 경우 0을 출력하도록 한다.
```python
# 출력
for a in range(n):
    for b in range(n):
        if graph[a][b]:
            print(1,end = " ")
        else:
            print(0,end = " ")
    print()


```
### 시간 복잡도
- 플루이드 워샬 알고리즘을 벗어나는 시간 복잡도가 없으므로 : `O(N^3)`
>>>>>>> main
