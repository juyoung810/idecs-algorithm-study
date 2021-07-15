#초기세팅 & 입력받기
n = int(input())
loc = [1,1]
paths = input().split()

for path in paths:
    if path == 'R' and loc[1] + 1 <= n:
        loc[1] += 1
    elif path == 'L' and loc[1] - 1 >= 1:
        loc[1] -= 1
    elif path == 'U' and loc[0] - 1 >= 1:
        loc[0] -= 1
    elif path == 'D' and loc[0] + 1 <= n:
        loc[0] += 1

print(loc[0], loc[1])


