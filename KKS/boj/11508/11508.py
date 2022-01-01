N = int(input())
price = []
ans = 0
for i in range(N):
    price.append(int(input()))
price.sort(reverse = True)

for i in range(N):
    if i % 3 == 2:
        continue
    ans += price[i]

print(ans)
