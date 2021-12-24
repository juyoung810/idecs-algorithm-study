# 연결된 덩어리가 몇 개 인지 판별 -> DFS 이용
# 연결 정보 주어진다 -> 연결 리스트로 구현

# 전체 컴퓨터 수 입력 받는다.
N = int(input())
# 0 ~ N 까지의 노드의 각각 연결 정보를 저장하기 위한 이중 배열 생성
connect = [[] for _ in range(N + 1)]
# 전체 연결된 짝의 수를 입력 받는다.
for _ in range(int(input())):
    n, m = map(int, input().split())
    # 양 노드의 연결리스트에 각각 연결 정보를 저장한다.
    connect[n].append(m)
    connect[m].append(n)

visited = [False for _ in range(N + 1)]


def DFS(start, connect, visited):
    # 시작 노드 True 설정
    visited[start] = True
    #print(start)
    for i in range(len(connect[start])):
        if not visited[connect[start][i]]:
            DFS(connect[start][i], connect, visited)
    # 연결 리스트가 끝났으면 return
    return

DFS(1,connect,visited)
# True의 갯수를 센다. 1 제외
print(visited.count(True)-1)
