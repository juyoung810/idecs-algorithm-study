### 평범한 배낭
## 무게와 가치를 가지는 물건들. 배낭에 넣을 수 있는 물건들의 가치의 최댓값은?

# 필요한 물건 n개와 버틸 수 있는 무게 k 입력받기
n, k = map(int, input().split())

# 물품 정보 입력받을 리스트와 결과 저장할 이중배열 만들기
products = [[0,0]]   # w, v 순
d = [[0]*(k+1) for _ in range(n+1)]

# 물품 정보 입력받기
for things in range(n):
    products.append(list(map(int, input().split())))

# 물품의 인덱스에 대해, 물품의 무게와 인덱스 값이 같거나 크면 가치를 집어넣기.
for i in range(1, n+1):
    for j in range(1, k+1):
        w = products[i][0]
        v = products[i][1]
        if w > j:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)

print(d[-1][-1])
