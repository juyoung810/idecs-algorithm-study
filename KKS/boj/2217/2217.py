n = int(input())
ropes = []

for i in range(n):
    ropes.append(int(input()))
ropes.sort()

ans = 0
for rope in ropes:
    if rope*n > ans:
        ans = rope*n
    n -= 1

print(ans)

