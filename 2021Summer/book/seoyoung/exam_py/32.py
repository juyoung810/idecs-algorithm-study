'''
## 정수 삼각형
> 문제 주소 : https://www.acmicpc.net/problem/1932

### 1. 문제
- 맨 위층부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라.
- 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택 가능

### 2. 문제 해결 방향
- 31번과 마찬가지로 각 칸에 대해서 최대값을 저장하고, 맨 아래줄에서 가장 큰 값을 출력하면 될 것 같다.
- 근데 삼각형 구조기 때문에 어떤 식으로 저장해야할지를 생각해보자.
- nxn 배열을 만들어서 초기화하고, 아래와 아래 오른쪽으로 더해서 더 큰 값을 저장한다.
'''

n = int(input())
dp = []

for _ in range(n):
    dp.append(list(map(int, input().split())))

# 다이나믹 프로그래밍
for i in range(1, n):
    for j in range(i+1):
        # 왼쪽 위
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i-1][j-1]
        # 바로 위
        if j == 1:
            up = 0
        else:
            up = dp[i-1][j]
        # 최대 합을 저장
        dp[i][j] = dp[i][j] + max(up_left, up)

print(max(dp[n-1]))

