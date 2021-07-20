n,m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y):
    # 범위가 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
            return False
    # 아직 방문하지 않았을 경우
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상하좌우 모두 재귀적으로 방문
        graph(x-1,y)
        graph(x,y-1)
        graph(x+1,y)
        graph(x,y+1)
        # 어쨋든 하나라도 0이면 return True 해준다.
        return True
    # 하나라도 0 아니면 return False
    return False

# ㅁ든 노드에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i,j) == True:
            result+=1

print(result)