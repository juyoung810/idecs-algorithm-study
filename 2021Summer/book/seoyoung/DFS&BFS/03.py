### 음료수 얼려 먹기
## 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램 작성
## 해당 노드와 연결된 모든 노드를 탐색하는 것이기 때문에 깊이 우선 탐색!

# 그래프로 모델링

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출. 행렬 구조 생각하기!! 인덱스로 호출하는 것. dfs는 스택 구조~ 재귀함수로 구현. 주변에 있는거 집어넣은 다음에 끝까지 간다...!
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:  # 방문 하지 않은 노드가 있을때! 1회씩 추가
            result += 1

print(result)

# 어렵다..!! 그래프의 구조와 문제를 해결하기 위해서는 어떤 탐색 방법을 택해야 하는지 고민하기. 또 어떤식으로 응용해야 하는지 고민하기