### 좌표 압축
## 수직선 위에 N개의 좌표 x1, x2, ..., xn이 있고, 이 좌표에 좌표 압축을 적용하려고 한다.
## xi를 좌표 압축한 결과 x'i는 xi > xj를 만족하는 서로 다른 좌표의 개수와 같아야함
## 좌표압축 적용한 결과를 출력해보자!
# 자기보다 작은 개수를 출력하면 됨.

import sys

# 좌표 개수
n = int(sys.stdin.readline())
coor = list(map(int, sys.stdin.readline().split()))

# 작은 값 기록할 배열을 새로 만든다.
smaller_x = []

# 좌표를 중복제거하고 정렬하기
sorted_set = sorted(list(set(coor)))

for i in range(n):
    idx = sorted_set.index(coor[i])
    smaller_x.append(idx)

for x in smaller_x:
    print(x, end=' ')