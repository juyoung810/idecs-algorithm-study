N = int(input())
ans = 0
workout = list(map(int, input().split()))
workout.sort()

if N%2 == 0:
    mid = N//2
    for i in range(0, mid):
        _temp = workout[i] + workout[N-1-i]
        ans = max(ans,_temp)
else:
    mid = (N-1)//2
    for i in range(0, mid):
        _temp = workout[i] + workout[N - 2 - i]
        ans = max(ans, _temp)
        ans = max(ans, workout[-1])

print(ans)