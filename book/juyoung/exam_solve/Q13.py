# 치킨 배달
# 치킨 거리 = 집과 가장 가까운 치킨집 사이의 거리 -> 집 기준으로 정해진다. -> 모든 집은 치킨 거리를 가진다.
# 도시 치킨 거리 = 모든 집의 치킨 거리의 합
# 0: 빈칸, 1: 집, 2: 치킨 거리
# 가자 많은 수익을 낼 수 있는 치킨 집 개수는 최대 M개 -> M개 제외 전부 폐업
# 어떻게 M개 고르면 도시 치킨 거리 가장 작을지 구하시오
# 2<N<=50, 1<=M<=13
import sys
from itertools import combinations

input = sys.stdin.readline


def find_min(chicken):
    global min_length
    for temp in chicken:
        sum_result = 0
        for home in homes:
            result = 1000000001
            for c in temp: # 3개 남은 조합 내에서 최소
                # 한가지 조합에서 모든 치킨집에 대한 한 치킨집 거리 -> 최소
                result = min(result, abs(home[0] - c[0]) + abs(home[1] - c[1]))
            sum_result += result
        # 모든 집에 대한 치킨 집 거리 합 == 도시 치킨 거리 최소
        min_length = min(min_length, sum_result)



def find_x(cnt):
    find_min(list(combinations(chickens, cnt))) # 남은 치킨


# n,m 입력 받기
n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

chickens = []
homes = []
# 치킨집 좌표 담기
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            homes.append([i, j])
        elif data[i][j] == 2:
            chickens.append([i, j])

# 최대 0 ~ M개 도시치킨거리 각각 구하기
min_length = 1000000001
for x in range(1,m+1):  #최대 1 ~ m개의 치킨집 남는다.
    find_x(x)

print(min_length)
