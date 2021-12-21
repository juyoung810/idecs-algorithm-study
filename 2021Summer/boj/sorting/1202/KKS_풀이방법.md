# boj 1202: 보석 도둑
> 문제 주소: https://www.acmicpc.net/problem/1202

### 문제설명
- 도둑이 있는데 도둑이 준비성이 좋아 가방을 여러개 가지고 다니고 심지어 가방마다 넣을수 있는 최대 무게가 다르다..
- 도둑은 욕심쟁이여서 가장 가치가 크게 훔치고싶다.. 
- 보석의 무게와 가치가 주어지고 가방의 최대 무게가 정해질때 도둑이 얼마까지 훔칠수 있을까?
뭐 대충 이런내용이다.

### 문제접근
- 훔친 가치를 maximize하기 위해선 기본적으로 비싼걸 훔처야됨 또 가벼운걸 훔쳐야됨
- 그렇기 위해선 작은 가방부터 담아야됨
- sort를 이용해서 정렬하고 하나씩 담아봤는데 시간초과가뜸

### 필요 내용
- max heap, min heap
- https://www.daleseo.com/python-heapq/ 여기 참고! heap에 대한 내용
- 파이썬의 힙은 min heap이고 가장 작은 수가 인덱스 0번에 위치

#### 코드구현
### 1. 필요정보 입력받기
```python
import sys
import heapq
input = sys.stdin.readline
from collections import deque
#보석의 총 개수 N, 가방의 총 개수 K
n , k = map(int, input().split())
arr = []
ruck = []
for i in range(n):
    #무게, 가격 입력
    arr.append(list(map(int, input().split())))
for i in range(k):
    #가방마다 담을수 있는 무게
    ruck.append(int(input()))
```

### 2. 정렬, 힙 선언 등..
```python
arr = deque(sorted(arr, key = lambda x : x[0])) #무게에 대해 오름차순 정렬
heap = []
ruck.sort()
```

### 3. 반복진행/ 결과출력
``` python
value = 0
for weight in ruck: #가방의 무게를 순회하면서
    while arr and weight >= arr[0][0]: #훔칠보석이 남아있고, 가방의 무게가 보석의 무게보다 더 크면
        heapq.heappush(heap, -arr.popleft()[1]) #힙에 무게push min힙이기때문에 -를 붙혀줌 그러면 결국 가장 가치가 큰 값이 0번째 인덱스에 있음
    if heap:
        value -= heapq.heappop(heap)#다시 -붙혀서 pop
print(value)
```