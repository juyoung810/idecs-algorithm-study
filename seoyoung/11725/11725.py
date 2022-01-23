'''
< 트리의 부모 찾기 >

루트 없는 투리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하자.

< 아이디어 >
1. 부모노드를 저장하는 리스트를 만든다.
2. 연결된 두 정점을 확인한다. 뒤의 노드값에 앞의 노드를 부모로 저장한다.
3. 만약 이미 저장되어 있으면, 앞의 노드값에 뒤의 노드를 부모로 저장한다.
4. 만약 두 값 중 1이 있으면, 나머지 값에 1을 저장한다.
5. 근데 이걸 dfs나 bfs로~
'''

# 이렇게 하면 틀린다! 결과는 나오지만...
n = int(input())
p_node = [0] * n

for _ in range(n-1):
    a, b = map(int, input().split())
    if a == 1:
        p_node[b-1] = 1
    elif b == 1:
        p_node[a-1] = 1
    if p_node[b-1] == 0:
        p_node[b-1] = a
    elif p_node[a-1] == 0:
        p_node[a-1] = b

for p in p_node[1:]:
    print(p)



# 굳이 dfs로 안해도 풀릴 것 같은데...
n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

for nodes in tree[2:]:
    print(nodes[0])



# bfs로 풀기
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
tree = [[] for _ in range(n+1)]
p_node = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def bfs(v, tree):
    queue = deque([v])
    while queue:
        idx = queue.popleft()
        for i in tree[idx]:
            if p_node[i] == 0:
                p_node[i] = idx
                queue.append(i)

bfs(1, tree)
for i in range(2, n+1):
    print(p_node[i])