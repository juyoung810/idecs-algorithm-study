N = int(input())
line = []
for i in range(N):
    line.append(int(input()))
line.sort(reverse=True)
ans = 0
for i in range(N):
    temp = (line[i] - i)
    if temp < 0:
        temp = 0
    ans += temp
print(ans)