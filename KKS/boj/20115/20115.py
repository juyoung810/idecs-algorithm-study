N = int(input())
drinks = list(map(int, input().split()))
drinks.sort()
ans = drinks[-1]
for i in range(N-1):
    ans += (drinks[i]/2)

print(ans)
