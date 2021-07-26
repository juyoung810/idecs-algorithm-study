# boj: 랜선 자르기
> 문제 주소: https://www.acmicpc.net/problem/1654
> 
> silver 3

### 1.문제 설명
-  책의 떡 자르기, 다른 백준문제의 나무 자르기 문제와 유사
-  매개변수 탐색 개념을 이진탐색으로 구현하면됨

### 2.유의점
-  최소값을 0 으로 설정하면 안됨 1로 설정해야함

### 3.코드구현
``` python
import sys
input = sys.stdin.readline
#k:이미 가지고있는 랜선의 개수, n:필요한 랜선의 개수
k, n = map(int, input().split())
arr = []
for i in range(k):
    arr.append(int(input()))
arr.sort()
#[802 743 457 539] -> 200
#랜선을 특정수로 나누고 몫을 취함, 그리고 이 몫의 합이 n보다 커야됨
#기존에 해오던 parametric search를 해보자!

low = 1
high = max(arr)

while low <= high:
    lan = 0
    guess = (low + high)//2
    for item in arr:
        lan += item//guess
    if lan < n:
        high = guess-1
    else:
        low = guess+1

print(high)
```