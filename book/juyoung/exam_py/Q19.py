import sys

input = sys.stdin.readline


def dfs(cnt, result, plus, minus, mul, div):
    global max_result
    global min_result
    if cnt == n:  # 모든 숫자 다 계산했을 경우
        max_result = max(max_result, result)
        min_result = min(min_result, result)
    if plus:  # plus가 0이 아닐 경우
        dfs(cnt + 1, result + data[cnt], plus - 1, minus, mul, div)
    if minus:
        dfs(cnt + 1, result - data[cnt], plus, minus - 1, mul, div)
    if mul:
        dfs(cnt + 1, result * data[cnt], plus, minus, mul - 1, div)
    if div:
        if result < 0:
            result = -((-result) // data[cnt])
        else:
            result = result // data[cnt]
        dfs(cnt + 1, result, plus, minus, mul, div - 1)


n = int(input())
data = list(map(int, input().split()))
# +,-,x,%
op = list(map(int, input().split()))
# 최댓값
max_result = -1000000001
min_result = 1000000001
dfs(1, data[0], op[0], op[1], op[2], op[3]) # 1개의 숫자는 계산이 됐다.
print(max_result)
print(min_result)
