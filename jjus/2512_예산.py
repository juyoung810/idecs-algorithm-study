import sys

input = sys.stdin.readline

N = int(input())
moneys = list(map(int, input().split()))
m_money = int(input())


def p_money():
    result = 0
    for m in moneys:
        if m > mid:
            result += mid
        else:
            result += m
    return result


start = 0 # 0 부터 시작
end = max(moneys)
ans = N
while start <= end:
    mid = (start + end) // 2
    if p_money() <= m_money:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)
