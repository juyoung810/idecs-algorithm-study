T = int(input())
ans = []
for i in range(T):
    N = int(input())
    stickers = []
    for i in range(2):
        stickers.append(list(map(int, input().split())))
    if len(stickers[0]) == 1:
        ans.append(max(stickers[0][0], stickers[1][0]))
    else:
        stickers[0][1] += stickers[1][0]
        stickers[1][1] += stickers[0][0]
        for i in range(2,N):
            stickers[0][i] += max(stickers[1][i-1], stickers[1][i-2])
            stickers[1][i] += max(stickers[0][i - 1], stickers[0][i - 2])
        ans.append(max(stickers[0][N-1], stickers[1][N-1]))

for j in ans:
    print(j)

