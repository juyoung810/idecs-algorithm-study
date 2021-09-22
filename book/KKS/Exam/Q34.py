N = int(input())
line = list(map(int, input().split()))
line.reverse()

# 1 로 초기화 하는 이유는 적어도 자기 자신은 존재하기 때문.
dp = [1] * N

for i in range(1, N):
    # dp[i] = i 를 마지막 원소로 가지는 부분 수열의 최대 길이
    for j in range(0, i):
        # 0~j까지의 dp를 살피며 arr[i]가 더 크면 dp[j] + 1
        # + 1은 arr[i]를 포함해야 하기 때문임.
        if line[j] < line[i]:
            dp[i] = max(dp[i], dp[j] + 1)
# max(dp) = lis.
print(N - max(dp))
