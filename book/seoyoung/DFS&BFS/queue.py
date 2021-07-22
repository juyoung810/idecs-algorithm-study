# 선입선출 구조.

from collections import deque

# 큐 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

queue = list(queue)
print(queue)     # 먼저 들어온 순서대로 출력
queue.reverse()  # 다음 출력을 위해 역순으로 바꾸기
print(queue)     # 나중에 들어온 원소부터 출력

# deque 객체를 리스트 자료형으로 변경하려면 list() 메서드 이용하기.