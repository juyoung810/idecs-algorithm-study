### ATM
## 인하은행 한 대의 ATM. 사람은 1~N번까지 번호 매겨져 있음. i번 사람이 돈 인출하는데 걸리는 시간은 Pi분.
## 사람들이 줄을 서는 순서에 따라 돈을 인출하는데 필요한 시간의 합이 달라짐. 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값은?

n = int(input())
P = list(map(int, input().split()))

# 오래 걸리는 사람이 돈을 늦게 인출해야 기다리는 시간이 짧아짐. 짧게 걸리는 순서대로 정렬
P.sort()   # sort 함수 시간복잡도 O(NlogN)
wait = 0
result = 0

for time in P:
    wait += time
    result += wait

print(result)