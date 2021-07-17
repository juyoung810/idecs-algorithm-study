n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
cnt = 0
value = 0
while True:
    for i in range(k):
        if cnt == m:
            break
        value += data[-1]
        cnt += 1
    if cnt == m:
        break
    value += data[-2]
    cnt += 1
print(value)
