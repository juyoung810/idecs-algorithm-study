# 0 0 1 2 3
# 1 0 1 2 3

# 1. (0,0) , (1,0) 중에 더 큰 것
# 2. (1,0), (2,0) 중에 더 큰 것
# 3. (0,0) 이랑 (1,2) 더한 것 VS (0,1) 이랑 (1,2) 더한 것 중에 큰 것을 (1,2)로 지정
# 4. (1,0) 이랑 (0,2) 더한 것 VS (1,0) 이랑 (0,2) 더한 것 중에 더 큰 것을 (0,2)로 지정한다.
# ...
# 마지막 column 에서 둘 중에 더 큰 값이 최댓값이다.
import sys
t = int(sys.stdin.readline())
for _ in range(t):
    N = int(sys.stdin.readline())
    stickers = []
    # 스티커 점수 입력 받기
    stickers.append(list(map(int,sys.stdin.readline().split())))
    stickers.append(list(map(int, sys.stdin.readline().split())))

    # 각 경우 최댓값 기록 위한 dp table 생성
    dp = []
    dp.append([0] * N)
    dp.append([0] * N)


    for i in range(N):
        # column 0 초기화
        if i == 0:
            dp[0][0] = stickers[0][0]
            dp[1][0] = stickers[1][0]
        elif i == 1:
            # column 1 초기화
            dp[0][1] = dp[1][0] + stickers[0][1]
            dp[1][1] = dp[0][0] + stickers[1][1]
        # row 0 비교 후 update
        else:
            if dp[1][i-2] + stickers[0][i] >= dp[1][i-1] + stickers[0][i]:
                dp[0][i] = dp[1][i-2] + stickers[0][i]
            else: dp[0][i] = dp[1][i-1] + stickers[0][i]

            # row 1 비교 후 update
            if dp[0][i-2] + stickers[1][i] >= dp[0][i-1] + stickers[1][i]:
                dp[1][i] = dp[0][i-2] + stickers[1][i]
            else: dp[1][i] = dp[0][i-1] + stickers[1][i]


    sys.stdout.write(str(max(dp[0][N-1],dp[1][N-1])) + "\n")


