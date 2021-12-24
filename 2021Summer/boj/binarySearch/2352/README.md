# boj 2352 : 반도체 설계 by KKS
> 문제 주소: https://www.acmicpc.net/problem/2352
> 
> gold 2

# 1.문제설명
- 리스트를 입력받는다
- 리스트의 인덱스가 from 포트고 리스트내 해당인덱스의 값이 to 포트이다
- 이렇게 선을 연결할때 겹치지않도록 최대 몇개까지 꽂힐수 있을까를 알아보는것이다

## 2.문제해결 아이디어.
- 혼자 생각못함
- LIS라는 유형의 문제

### 3.문제접근법
- LIS(Longest Increasing Subsequence)라는 유명한 유형
- 해결방법은 2가지가 있다. DP(Dynamic Programming)을 이용하는 방법 그리고 이진탐색을 이용하는방법
- DP는 수열 원소의 개수가 많아지면 시간초과가 나올수 있다. 따라서 이진탐색을 이용해본다.

### 4.LIS구하는 알고리즘
참조 https://t-anb.tistory.com/44
- 빈 리스트를 생성(편의를 위해 LIS라고 정의)
- 주어진 수열의 원소들을 순회하며 아래와같은 조건문을 진행
- 만약에 LIS가 비었거나, LIS의 마지막원소보다 현재 순회하는 원소가 크면
- LIS에 현재 순회중인 원소를 append
- 아니라면(현재 순회중인 원소가 작으면)
- 이분탐색을 통해 LIS에 그 원소가 들어갈 인덱스를 찾고 그 인덱스에 삽입한다(기존의 값을 업데이트)  
이분탐색을 사용할수 있는 이유는 LIS의 구성이 정렬되어있기 때문에 사용이 가능하다

### 5.코드구현
``` python
import sys
input = sys.stdin.readline
n = int(input())
connection = list(map(int,input().split()))
lis = []

def lowerbound(lis,x):
    start, end = 0, len(lis)-1

    while start <= end:
        mid = (start+end)//2
        if lis[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return start

for x in connection:
    if not lis or lis[-1] < x:
        lis.append(x)
    else:
        lis[lowerbound(lis,x)] = x

print(len(lis))
```