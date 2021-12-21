import sys
input = sys.stdin.readline
n = int(input())
times = [0] * (n+1) #해당작업에 걸리는 시간
graph = {} #key: n번째 작업, value = n번째 작업을 위한 선행작업
for i in range(1, n+1):
    lst = list(map(int, input().split()))
    times[i] = lst[0]
    if lst[1] == 0: # 선행작업들이 없으면
        continue # 패스
    for j in lst[2:]: #선행작업들이 있으면
        if i in graph: #i번째 작업에 j를 추가해줌
            graph[i].append(j)
        else: #없으면 [j]를 만듬
            graph[i] = [j]

for i in range(1, n+1):
    if i in graph:
        time = 0
        for j in graph[i]:
            time = max(time, times[j])
        times[i] += time

print(max(times))