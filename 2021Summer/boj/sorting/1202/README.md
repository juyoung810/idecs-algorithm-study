# <span style="color:red">boj 1202: 보석 도둑 by juyoung</span>
> 문제 주소: https://www.acmicpc.net/problem/1202
> 
> gold 2


## 문제 해결 방향
1. 보석을 입력 받아 무게를 기준으로 오름차순 정렬한다.
2. 가방을 입력 받아 무게를 기준으로 오름차순 정렬한다. -> 가방의 무게가 작은 것 부터 넣어야 하므로 
3. 크기가 N인 priority Queue 생성한다. -> 가방에 넣고나서, 이미 들어있는 보석은 다음 가방에도 당연히 들어갈 수 있으므로
4. 가방의 갯수만큼 반복문을 돈다.
5. 반복문 내에서,  __가방의 무게보다 작거나 같은 것의 보석의 가치를 MAX HEAP__ 에 집어 넣는다
    `pq.put(-1 * value)`
   
6.  Max heap에서 가치가 가장 큰 것을 get해서 최종 결과에 더한다.
```python
from queue import PriorityQueue
import sys
N, K = map(int, sys.stdin.readline().split())
jewels = []
bags = []

# 보석 받아서,
for _ in range(N):
    jewels.append(tuple(map(int, sys.stdin.readline().split())))

for _ in range(K):
    bags.append(int(sys.stdin.readline()))

# 보석 무게 오름차순 정렬
jewels.sort(key=lambda x: x[0])
# 가방 무게 오름차순 정렬
bags.sort()
sum = 0
# 보석을 한 바퀴만 돈다-> 이미 pq 에 들어있는 것 다음 가방에도 당연히 들어갈 수 있으므로
jewel_idx = 0
pq = PriorityQueue(N)
# 가방의 수 만큼 반복한다.
for i in range(K):
    while jewel_idx < N and jewels[jewel_idx][0] <= bags[i]:
        # 가방의 무게보다 보석의 무게가 작거나 같으면 , max PQ에 넣기
        pq.put(-jewels[jewel_idx][1])
        jewel_idx += 1

    if not pq.empty():
        sum += -pq.get()

sys.stdout.write(str(sum))

```
## 알게된 점
### PriorityQueue(heap)
`from queue import PriorityQueue`
1. 생성 방법: `pq.PriorityQueue()`
2. 삽입 방법: `pq.put(key,value) or pq.put(value)` -> __오름차순으로 자동 정렬되어 저장된다.__
3. 제거 방법: `pq.get()` -> 오름차순으로 pop() 되면서 값 return
#### 시간복잡도:  O(log N)