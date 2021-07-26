### 좌표 압축
## 수직선 위에 N개의 좌표 x1, x2, ..., xn이 있고, 이 좌표에 좌표 압축을 적용하려고 한다.
## xi를 좌표 압축한 결과 x'i는 xi > xj를 만족하는 서로 다른 좌표의 개수와 같아야함
## 좌표압축 적용한 결과를 출력해보자!
# 자기보다 작은 개수를 출력하면 됨.

import sys

# 좌표 개수
n = int(sys.stdin.readline())
coor = list(map(int, sys.stdin.readline().split()))

# 작은 값 기록할 배열을 새로 만든다. 좌표 개수만큼
smaller_x = [[] for i in range(n)]

# 원소들에 대해서 해당 원소보다 작으면 해당 인덱스에 값 더해주고 그 배열 출력하기
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if coor[i] > coor[j]:
            smaller_x[i].append(coor[j])

for x in smaller_x:
    x = set(x)   # 중복 제거
    print(len(x), end=' ')