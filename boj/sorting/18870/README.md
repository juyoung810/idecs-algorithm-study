# boj 18870: 좌표 압축 by seoyoung
> 문제 주소: https://www.acmicpc.net/problem/18870
> 
> silver 2

## 좌표압축
수직선 위에 N개의 좌표 x1, x2, ..., xn이 있고, 이 좌표에 좌표 압축을 적용하려고 한다.
 xi를 좌표 압축한 결과 x'i는 xi > xj를 만족하는 서로 다른 좌표의 개수와 같아야함.
 좌표압축 적용한 결과를 출력해보자!

## 문제 해결 방향
1. 자기보다 작은 좌표의 개수를 출력해야 한다.
2. 중복이 있을 수 있으므로 set을 이용해 중복을 제거하고, sort로 정렬해 해결한다.
```python
import sys

# 좌표 개수
n = int(sys.stdin.readline())
coor = list(map(int, sys.stdin.readline().split()))

# 좌표를 중복제거하고 정렬하기
sorted_set = sorted(list(set(coor)))
```
3. 좌표 압축 결과를 딕셔너리로 표현한다. enumerate 함수를 이용하면 인덱스와 값을 얻을 수 있다.
정렬된 인덱스, 값을 반대로 넣어주어 값에 따른 인덱스 값을 알 수 있도록 한다.

```
# 좌표 압축 결과 딕셔너리로 표현. enumerate는 인덱스와 원소를 뽑아주는 함수
xt = {value:index for index, value in enumerate(sorted_set)}
```
4. 입력받았던 좌표 리스트의 각 좌표에 대해, 압축 결과를 출력한다. 좌표 압축 결과를 담은 딕셔너리에 좌표가 key로 들어가있기 때문에, 좌표를 입력하면 인덱스가 출력된다.


```
for xi in coor:
    print(xt[xi], end=' ')
```


### 타임아웃 버전..1
1. 좌표보다 작은 값을 입력할 배열을 만들고, 각 좌표에 대해 더 작으면 해당 인덱스의 배열에 값을 더해준다.
2. 각 인덱스의 배열에 대해 중복제거하고, 그 길이를 출력한다.

```python
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
```

### 타임아웃 버전..2

1. 좌표보다 작은 값을 기록할 배열을 만든다.
2. 좌표를 중복 제거하고 정렬한 새로운 배열을 만든다.
3. 중복제거하고 정렬한 배열에서, 원래 좌표의 인덱스 위치를 반환해 smaller_x 리스트에 추가한다.

```python
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
```