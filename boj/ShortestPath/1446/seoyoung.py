'''
지름길
운전해야 하는 거리의 최솟값은?
일방통행. 지름길의 개수 N과 고속도로의 길이 D가 주어진다.
시작에서 각 위치까지의 최솟값을 구한다.
'''

n, d = map(int, input().split())
# 도로 길이와 같은 리스트를 만들어준다. 각 위치는 자기 자신의 값을 갖는다.
highway = [i for i in range(d+1)]

# 지름길을 입력받는다. 시작위치, 도착위치, 지름길의 길이
shortcut = []
for _ in range(n):
    s, e, l = map(int, input().split())
    if e <= d:
        shortcut.append([s, e, l])

# 도로의 값에 대해서 확인한다. 자신의 값과, 바로 전에 1을 더한 값 중 더 작은 값을 넣는다.
# 만약 시작 인덱스가 지름길에 있는 값이라면, 도착 위치의 인덱스의 값으로 가서 시작 인덱스에 지름길의 길이를 더한 값을 넣는다.
for i in range(d+1):
    highway[i] = min(highway[i], highway[i-1]+1)
    for j in shortcut:
        if i == j[0]:
            highway[j[1]] = min(highway[j[1]], highway[i] + j[2])

print(highway[-1])