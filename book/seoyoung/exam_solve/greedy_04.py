'''
< 만들 수 없는 금액 >
n개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램을 작성하라.
만약 동전 중에 1이 없으면 무조건 1.
만약 동전 중에 1이 있으면 n개의 동전을 이용해 만들 수 있는 모든 경우의 수를 만든다.
부분집합을 생성해서, 1부터 확인한다. 만약 부분집합 리스트에 없으면 그 수를 출력한다.
근데 이렇게 하는건 greedy는 아님. 뭔가 백준으로 했으면 시간초과 떴을 듯
'''

n = int(input())
coins = sorted(list(map(int, input().split())))

subset = [[]]
cases = []

for coin in coins:
    size = len(subset)
    for y in range(size):
        subset.append(subset[y] + [coin])

subset = subset[1:]

for case in subset:
    cases.append(sum(case))

for i in range(1, 2**n-1):
    # 만약 1이 없으면 1을 출력한다.
    if cases[0] != 1:
        print(1)
        break

    if i in cases:
        continue
    else:
        print(i)
        break


# 그리디로 푸는 방법 : 만들 수 있는 수인지 확인한다.
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

print(target)