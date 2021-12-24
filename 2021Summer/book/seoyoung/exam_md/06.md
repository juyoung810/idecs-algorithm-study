## 만들 수 없는 금액 
- n개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램을 작성하라.

### 문제 해결 방향
- 만약 동전 중에 1이 없으면 무조건 1.
- 만약 동전 중에 1이 있으면 n개의 동전을 이용해 만들 수 있는 모든 경우의 수를 만든다.
- 부분집합을 생성해서, 1부터 확인한다. 만약 부분집합 리스트에 없으면 그 수를 출력한다.
- 근데 이렇게 하는건 greedy는 아님. 뭔가 백준으로 했으면 시간초과 떴을 듯
- greedy로 하는 방법은 책의 방법을 참고해서 그대로 했다.


### 소스코드

- 입력을 받고, 동전들의 모든 부분집합을 저장할 배열과 각 부분집합의 합을 저장할 배열을 만든다.
```python
n = int(input())
coins = sorted(list(map(int, input().split())))

subset = [[]]
cases = []
```
- 모든 부분집합을 생성하는 코드. 모든 동전에 대해서, 모든 부분집합에 더해준다.
- 부분집합의 첫 원소는 공집합이다. 필요없으니까 빼준다.
```python
for coin in coins:
    size = len(subset)
    for y in range(size):
        subset.append(subset[y] + [coin])

subset = subset[1:]
```
- 각 부분집합의 합을 저장해준다.
```python
for case in subset:
    cases.append(sum(case))
```
- 만약 부분집합의 합에 1이 없으면 1을 출력하고, 아니면 수를 하나씩 늘려가며 부분집합의 합 배열에 들어있는지 확인한다.
- 없으면 그 값을 출력한다.
- 지금 보니 range 값을 잘못 설정한 것 같은데, 저건 부분집합의 수만큼 돌아가게 한 것. 근데 그럴 필요 없는 것 같다. 대충 큰 수 넣으면 될듯 100정도

```python
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
```

### 그리디로 푸는 방법 : 만들 수 있는 수인지 확인한다.
```python
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
```