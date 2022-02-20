n = int(input())
honey_list = list(map(int, input().split()))
s = [0 for _ in range(n+1)]

for i in range(1, n+1):
    s[i] = s[i-1] + honey_list[i-1] #누적합을 저장함
ans = 0

for k in range(2, n):
    temp = (s[k] - s[1]) + (s[-2] - s[k-1]) #벌들이 양 끝에있고 꿀통이 가운데 있을때
    ans = max(ans, temp)

for k in range(2, n):
    temp = (s[-2] - s[k]) + 2*(s[k-1] - s[0])
    ans = max(ans, temp)

for k in range(2, n):
    temp = (s[k-1] -s[1] + 2*(s[-1] - s[k]))
    ans = max(ans, temp)

print(ans)