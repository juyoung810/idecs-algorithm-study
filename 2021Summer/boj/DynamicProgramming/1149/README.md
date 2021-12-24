# boj 1149 : RGB거리 by KKS
> 문제 주소: https://www.acmicpc.net/problem/1149
> 
> 난이도: silver 1

## 1.문제설명
![img.png](img.png)

## 2.문제해결 아이디어.
- 2차원 배열의 그리드를 생각.(굳이 생성할 필요는 없음, 입력이 2차원으로 들어옴)
- row는 집의 갯수이고, column은 색을 의미한다.
- 배열의 값은 비용을 의미한다.

## 3.문제접근법
- 첫번째 row는 일단 pass
- 두번째 row부터 반복하며 이전 집의 색을 고려해 2가지 색의 경우의 비용을 고려
- ![img_1.png](img_1.png)
- 출처 : https://chunghyup.tistory.com/48

## 4.특별히 참고할 사항
- 2차원 그리드를 이용하는 생각.

## 5.코드구현
``` python
#집의 갯수 입력
n = int(input())
cost = []
for i in range(n):
    # R G B
    cost.append(list(map(int,input().split())))

#초기조건
for i in range(1, n):
    cost[i][0] = cost[i][0] + min(cost[i-1][1], cost[i-1][2])
    cost[i][1] = cost[i][1] + min(cost[i - 1][0], cost[i - 1][2])
    cost[i][2] = cost[i][2] + min(cost[i - 1][0], cost[i - 1][1])

print(min(cost[n-1][0],cost[n-1][1],cost[n-1][2]))
```