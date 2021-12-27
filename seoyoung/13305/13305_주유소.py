'''
일직선 도로 위의 N개의 도시가 있다. 제일 왼쪽의 도시에서 출발해 제일 오른쪽의 도시로 이동
처음 출발할때 주유소에서 기름 넣고 출발
각 도시별 주유소의 리터당 가격과 도로의 길이가 주어진다.
최소 비용을 계산하는 프로그램을 작성해보자!

< 아이디어 >
1. 입력 받아서 일직선으로 도로를 만든다. 리터당 가격으로 만든다.
2. 바로 앞의 인덱스의 값이랑 비교한다. 더 작으면 그걸로 바꾼다.
3. 다 더한다.
'''

# 도시의 개수
n = int(input())
road = ''
length = input().split()
cost = input().split()

# 도로 만들기
for i in range(len(length)):
    road += cost[i] * int(length[i])

road = [int(i) for i in road]

for i in range(1, len(road) - 1):
    if road[i] < road[i + 1]:
        road[i + 1] = road[i]

print(sum(road))

# 틀렸다는디 왜지

n = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

total = roads[0] * costs[0]
min_cost = costs[0]
dist = 0

for i in range(1, n-1):
    if costs[i] < min_cost:
        total += min_cost * dist
        min_cost = costs[i]
        dist = roads[i]
    else:
        dist += roads[i]

    if i == n-2:
        total += min_cost * dist

print(total)