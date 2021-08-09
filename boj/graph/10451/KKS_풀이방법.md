# boj 10451 : 순열사이클 by KKS
> 문제 주소: https://www.acmicpc.net/problem/10451
> 
> 난이도: silver2

## 1.문제설명
- 그래프 이론보다는 그냥 그래프 탐색이 더 맞는듯함.!?
## 2. 문제 접근법 
- 그래프탐색이라 union find알고리즘으로 카운트를 1씩 증가하며 해보려했지만 실패
## 3.문제 해결 아이디어 or 핵심
- DFS를 통하면 사이클 한 묶음을 찾을수 있음 

## 4.특별히 참고할 사항


## 5.코드구현
``` python
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(start):
    visited.add(start)
    next_node = path[start]
    if next_node not in visited:
        dfs(next_node)

tc = int(input())
for _ in range(tc):
    visited = set()
    ans = 0
    n = int(input())
    path =[0] + list(map(int, input().split()))
    visited.add(0)

    for i in range(1, n+1):
        if i not in visited:
            dfs(i)
            ans += 1
    print(ans)
```