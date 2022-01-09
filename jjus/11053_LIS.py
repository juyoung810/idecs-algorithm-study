"""
- i 번째에서 0 - (i-1) 까지 돌며 값이 자신 보다 작고, dp 값이 더 크다면 저장
- 마지막까지 돌았을때 0 일 경우 해당하는 것이 증가하는 수열에 속하지 못한 것 이므로 1로 초기화
- 0이 아닐 경우 어떠한 증가하는 수열에 속한 것 이므로 +1

156ms -> 더 작은 부분을 탐색할 때 이진 탐색을 사용할 경우 더 빨라질 수 있다.
"""
import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().rstrip().split(" ")))

dp = [0] * N
dp[0] = 1

for i in range(1, N):
    max_dp = 0
    for j in range(0,i):
        if arr[j] < arr[i] and dp[j] > dp[i]:
            dp[i] = dp[j]
    if dp[i] == 0: dp[i] = 1
    else: dp[i] += 1

#print(dp)
print(max(dp))