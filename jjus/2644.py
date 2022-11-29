import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(300000)
def dfs(arg1):
    for m_n in graph[arg1]:
        if visited[m_n] == 0: # 방문하지 않았을 경우
            visited[m_n] = visited[arg1] + 1# 방문 표시 & 몇 촌 내려왔는지 표시
            dfs(m_n)
    return
def bfs(arg1,arg2):
    q = deque()
    visited[arg1] = 1
    q.append([arg1,0])
    while q:
        m_n,count = q.pop()

        if m_n == arg2:
            return count
        for n_n in graph[m_n]:
            if not visited[n_n]:
                visited[n_n] = 1
                q.append([n_n,count+1])

    return -1

n = int(input()) # 사람 수
k1,k2 = map(int,input().rstrip().split()) # 괸계 구할 관계 두 명 번호
m = int(input()) # n들 간의 관계 수

# 양방향, 간선 weight = 1
graph = [[] for _ in range(n+1)]

for _ in range(m): # 관계 그래프에 입력
    p,c = map(int,input().rstrip().split()) # 부모, 자식
    graph[p].append(c)
    graph[c].append(p)

visited = [0] * (n+1)
print(bfs(k1,k2))
#dfs(k1)
#if visited[k2] == 0: print(-1)
#else: print(visited[k2])
#print(visited[k2] if visited[k2] > 0 else -1)

