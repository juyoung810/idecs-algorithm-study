'''
2+1 세일 행사. 유제품 세 개를 한 번에 사면 가장 싼 것은 무료
N개의 유제품을 모두 살 때 필요한 최소 비용을 출력하자!

< 아이디어 >
N개의 유제품을 내림차순 정렬한다. 3번재에 해당하는 제품을 제외하고 비용에 더한다.
'''

n = int(input())
costs = []
result = 0

for _ in range(n):
    costs.append(int(input()))

costs.sort(reverse=True)

for i in range(n):
    if (i+1)%3 == 0:
        continue
    result += costs[i]

print(result)