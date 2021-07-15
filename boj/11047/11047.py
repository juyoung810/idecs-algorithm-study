n, k = map(int, input().split())
data = []
cnt = 0
for i in range(n):
    _temp = int(input())
    data.append(_temp)
while True:
    if k  == 0:
        break
    else:
        cnt += k//data[-1]
        k = k % data[-1]
        data = data[:-1]
print(cnt)