# boj 10733 : 제로
> 문제 주소 : https://www.acmicpc.net/problem/10773

### 문제 해결 방향
- 가장 최근에 들어온 값이 없어지니깐 FILO인 스택 사용(LIFO)
입력받은 값 반복돌면서 리스트에 append해주다 0만나면 append하지 않고  
맨 마지막 값 pop하면됨
``` python
from collections import deque
queue = deque()
n = int(input())
for i in range(n):
    _temp = int(input())
    if _temp == 0:
        queue.pop()
    else:
        queue.append(_temp)
print(sum(queue))
```