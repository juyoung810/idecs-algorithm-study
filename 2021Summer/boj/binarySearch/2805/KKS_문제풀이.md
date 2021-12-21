# boj 2805: 나무 자르기
> 문제 주소: https://www.acmicpc.net/problem/2805
> 
> silver 3

### 1.문제 설명
-  책의 떡 자르기, 다른 백준문제의 랜선 자르기 문제와 유사
-  매개변수 탐색 개념을 이진탐색으로 구현하면됨

### 2.유의점
-  최소값을 0 으로 설정하면 안됨 1로 설정해야함

### 3.코드구현
``` python
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
data = list(map(int,input().split()))

low = 0
high = max(data)

result = 0
while low <= high:
    total = 0
    mid = (low + high)//2
    for item in data:
        if item > mid:
            total += (item-mid)
    if total < m:
        high = mid - 1
    else:
        result = mid
        low = mid+1
print(result)
```