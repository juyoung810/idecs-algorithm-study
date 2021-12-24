# boj 12015: 가장 긴 증가하는 부분 수열 2 
> 문제 주소: https://www.acmicpc.net/problem/12015
> 
> gold 2

### 문제설명
1. 수열이 주어졌을 때 가장 긴 부분수열을 구하는 문제

### 문제접근법
- LIS(Longest Increasing Subsequence)라는 유명한 유형
- 해결방법은 2가지가 있다. DP(Dynamic Programming)을 이용하는 방법 그리고 이진탐색을 이용하는방법
- DP는 수열 원소의 개수가 많아지면 시간초과가 나올수 있다. 따라서 이진탐색을 이용해본다.

### LIS구하는 알고리즘
참조 https://t-anb.tistory.com/44
- 빈 리스트를 생성(편의를 위해 LIS라고 정의)
- 주어진 수열의 원소들을 순회하며 아래와같은 조건문을 진행
- 만약에 LIS가 비었거나, LIS의 마지막원소보다 현재 순회하는 원소가 크면
- LIS에 현재 순회중인 원소를 append
- 아니라면(현재 순회중인 원소가 작으면)
- 이분탐색을 통해 LIS에 그 원소가 들어갈 인덱스를 찾고 그 인덱스에 삽입한다(기존의 값을 업데이트)  
이분탐색을 사용할수 있는 이유는 LIS의 구성이 정렬되어있기 때문에 사용이 가능하다

#### 코드구현
``` python
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
lis = []
#이분탐색 코드
def search_index(lis, x):
    start = 0
    end = len(lis) -1
    while start <= end:
        mid = (start + end) // 2
        if lis[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return start

#원소 순회
for item in arr:
    if not lis or lis[-1] < item:
        lis.append(item)
    else:
        idx = search_index(lis, item)
        lis[idx] = item

print(len(lis))

```