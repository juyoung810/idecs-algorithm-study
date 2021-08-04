# boj 12865: 평범한 배낭 by seoyoung
> 문제 주소: https://www.acmicpc.net/problem/12865
> 
> gold 5

## 문제
n개의 물건 중, 최대 k만큼의 무게를 넣을 수 있는 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 구하라.

## 문제 해결 방향
- [물건의 개수][배낭의 크기] 크기의 2중 배열을 만들어 해결한다.
- 먼저 물건을 들어가는 크기의 배낭에 다 넣어 가치를 기록한다.
- 직전 행의 같은 열에 해당하는 값을 넣고, 해당 열의 인덱스에서 물건의 무게를 뺀 인덱스에 해당하는 물건의 가치와 현재 행의 물건의 가치를 더해 비교해 더 큰 값을 넣는다.
- 사진 참고

## 소스코드
```python
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

```