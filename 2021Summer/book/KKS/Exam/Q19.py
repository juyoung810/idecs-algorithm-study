N = int(input())
data = list(map(int, input().split()))
# + - * /
oper = list(map(int, input().split()))
maximum = int(-1e9)
minimum = int(1e9)

def dfs(degree, total, plus, minus, multiply, divide):
    global maximum, minimum
    if degree == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(degree + 1, total + data[degree], plus -1, minus, multiply, divide)
    if minus:
        dfs(degree + 1, total - data[degree], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(degree + 1, total * data[degree], plus, minus, multiply - 1, divide)
    if divide:
        dfs(degree + 1, int(total / data[degree]), plus, minus, multiply, divide - 1)

dfs(1, data[0], oper[0], oper[1], oper[2], oper[3])
print(maximum)
print(minimum)