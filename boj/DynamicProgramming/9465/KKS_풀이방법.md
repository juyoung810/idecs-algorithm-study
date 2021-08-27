# boj 9465 : 스티커 
> 문제 주소: https://www.acmicpc.net/problem/9465
> 
> 난이도: silver 1

## 1.문제설명
- 2줄짜리 스티커를 때는데
- 스티커 때면 그 스티커와 변을 공유하는 스티커는 못땜
- 스티커에 적힌값이 최대가되게 뜯으면 몇점을 뜯을수있냐?

## 2.문제해결 아이디어.

- 처음에 무조건 대각선으로 가면 되지 않을까? -> Nope
- 대각선 말고도 답이 있다..

## 3.문제접근법

- 대각선 or 대각선 하나 옆도 체크해줘야됨

## 4.특별히 참고할 사항
- 사실 생각이안나서 구글에 검색함

## 5.코드구현
``` python
n = int(input())
ans = []
for _ in range(n):
  k = int(input())
  arr = []
  for _ in range(2):
    arr.append(list(map(int,input().split())))
  #길이가 1일때( k == 1)
  if k == 1:
    ans.append(max(arr[0][0],arr[1][0]))
  else:
    arr[0][1] += arr[1][0]
    arr[1][1] += arr[0][0]
    for i in range(2,k):
      arr[0][i] += max(arr[1][i-1],arr[1][i-2])
      arr[1][i] += max(arr[0][i-1],arr[0][i-2])
    ans.append(max(arr[0][k-1],arr[1][k-1]))

for j in ans:
  print(j)
```