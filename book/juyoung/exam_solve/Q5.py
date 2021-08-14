# 볼링공 고르기
# N개의 볼링공이 주어진다.
# 볼링공의 무게는 M개가 주어진다.
# 같은 무게의 공 여러개 존재할 수 있지만, 서로 다른 공으로 간주한다.
# 서로 다른 무게의 볼링공 고르는 경우의 수

# 내 생각
# N + 1크기의 배열 생성한다.
# 해당 배열 보다 큰 번호 이면서, 무게가 같지 않으면 count +1
#
# # n,m입력 받는다
# n , m = map(int,input().split())
#
# # 각각의 무게의 공 저장 위해 N 배열 생성
# balls = list(map(int,input().split()))
#
# count = 0
# for i in range(n):
#     for j in range(i,n):
#         if balls[i] != balls[j]:
#             count += 1
#
# print(count)

# O(n^2) 시간 -> 너무 오래 걸린다.


# 풀이
# 각 무게별로 가지는 공의 갯수 저장한다.
# A가 무게를 선택했을 때, B가 공을 고를 수 있는 공의 갯수 * 해당 무게 공의 수 를 다 더하면 총 경우의 수가 된다.
# B가 고를 수 있는 공의 갯수는 이전 무게에서 선택했던 경우를 제외해야한다.
# n을 A가 선택할 수 있는 개수를 계속 뺀다.
n,m = map(int,input().split())
balls = list(map(int,input().split()))

# 무게별 공의 수 센다.
array = [0] * 11 # 공의 무게는 1~ 10 까지
for ball in balls:
    array[ball] += 1

count = 0
for i in range(1,m+1):
    n -= array[i] # 이전에 count 한 경우를 빼기 위해
    count += array[i] * n

print(count)



# 시간 복잡도: O(m)