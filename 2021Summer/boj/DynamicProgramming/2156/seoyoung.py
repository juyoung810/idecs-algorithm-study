### 포도주 시식
## 책의 두번째 예제랑 같은 문제

n = int(input())
wine = []

for i in range(n):
    wine.append(int(input()))

d = [0] * n

if n == 1:
    print(wine[0])
elif n == 2:
    print(sum(wine))
else:
    d[0] = wine[0]
    d[1] = d[0] + wine[1]
    d[2] = max(d[1], d[0] + wine[2], wine[1] + wine[2])

    for j in range(3, n):
        d[j] = max(d[j-1], d[j-2] + wine[j], d[j-3] + wine[j-1] + wine[j])

    print(d[n-1])