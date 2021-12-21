# 1. row 0 이면 dp에 그대로 작성
# 2. column 0이면,
    # ex) row 1 column 0 : [0][자기] + 자기 VS [0][자기 + 1] + 자기
# 3. column 중간이면
    # ex) row 1 column 2 : [0][자기 -1] + 자기 VS [0][자기] + 자기 + [0][자기 +1]
# 4. column 끝이면
    # ex) row 1 column 3 : [0][자기] + 자기 VS [0][자기-1] + 자기


# 결과는 마지막 row에서 가장 큰 값, 가장 작은 값

import sys
N = int(sys.stdin.readline())


# 현재 줄, 다음 줄만 저장한다.
dp = [[0,0,0],[9,9,9]]

for i in range(N):
    down = list(map(int,sys.stdin.readline().split()))
    if i == 0:
        for j in range(3):
            dp[0][j] = down[j]
            dp[1][j] = down[j]
    else:
        # 최대 구하기
        a = dp[0][0]
        b = dp[0][1]
        c = dp[0][2]

        dp[0][0] = down[0] + max(a, b)
        # column 1 일 때
        dp[0][1] = down[1] + max(a, b, c)
        # column 2 일 때
        dp[0][2] = down[2] + max(b, c)

        # 최소 구하기
        a = dp[1][0]
        b = dp[1][1]
        c = dp[1][2]

        # column 0 일 때
        dp[1][0] = down[0] + min(a, b)
        # column 1 일 때
        dp[1][1] = down[1] + min(a, b, c)
        # column 2 일 때
        dp[1][2] = down[2] + min(b, c)


print(max(dp[0]),min(dp[1]))