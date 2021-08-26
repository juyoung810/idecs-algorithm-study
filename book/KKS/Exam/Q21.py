from collections import deque
N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
# 완전탐색을 함 (BFS) 이용
# 0,0부터 상하좌우 움직이면서 범위내에 있고 이동 조건을 만족하면
# -> cnt += 1, total에 누적 dfs 다 끝나면 이동한 좌표들 total // cnt로 값 다 바꿔줌
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0
# 국경을 개방하는 부분
def bfs(x,y):
    local_visited = {(x, y)}
    q = deque([(x,y)])

    total, cnt = 0, 0
    while q:
        x,y = q.popleft()
        total += graph[x][y]
        cnt += 1

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0<= ny < N and (nx, ny) not in local_visited and (nx, ny) not in total_visited:
                diff = abs(graph[nx][ny] - graph[x][y])
                if L <= diff <= R:
                    global is_move
                    is_move = True

                    q.append((nx, ny))
                    local_visited.add((nx, ny))

    return total//cnt, local_visited

while True:
    total_visited = set()
    is_move = False
    unions = []

    for i in range(N):
        for j in range(N):
            if (i,j) not in total_visited:
                new_num, visited = bfs(i,j)
                unions.append((new_num, visited))
                total_visited |= visited

    for (new_num, union) in unions:
        for country in union:
            x,y = country
            graph[x][y] = new_num

    if not is_move:
        break
    ans += 1
print(ans)
