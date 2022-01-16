'''
- dp table에 있는 값 누적 : 연속
- 앞의 수와 더하기 : 새로운 연속 시작
- 자기자신이 가장 큰 경우

140ms
'''
import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().rstrip().split(" ")))

dp = [0] * N
dp[0] = arr[0]
for i in range(1, N):
    if dp[i - 1] + arr[i] > arr[i - 1] + arr[i]:
        if arr[i] < dp[i - 1] + arr[i]:
            dp[i] = dp[i - 1] + arr[i]
        else:
            dp[i] = arr[i]
    else:
        if arr[i] < arr[i - 1] + arr[i]:
            dp[i] = arr[i - 1] + arr[i]
        else:
            dp[i] = arr[i]


#print(dp)
print(max(dp))
