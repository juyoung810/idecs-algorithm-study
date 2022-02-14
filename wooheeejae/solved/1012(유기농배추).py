#유기농배추
import sys
sys.setrecursionlimit(10000)

 # DFS함수 정의
def dfs(x, y):
    move = [0, -1, 0, 1, 0] # 상하좌우 확인용
    for i in range(4):
        xPoint = x + move[i]
        yPoint = y + move[i+1]
        if (0 <= xPoint < w) and (0 <= yPoint < h): # 배추밭을 벗어나지 않게함
            if graph[yPoint][xPoint] == 1: #
                graph[yPoint][xPoint] = -1 # 확인된 것 표기
                dfs(xPoint, yPoint)
 # 문제 풀이
case = int(input()) # 케이스 갯수
for i in range(case):
    w, h, num = map(int, input().split()) # 가로, 세로, 배추갯수
    graph = [[0] * w for i in range(h)] # 인접 행렬 만들기
    answer = 0 # 정답 초기화

    # 배추 심기
    for j in range(num):
        n, m = map(int, input().split())
        graph[m][n] = 1

    # DFS함수 적용
    for k in range(w):
        for l in range(h):
            if graph[l][k] == 1:
                dfs(k, l)
                answer += 1

    print(answer)
