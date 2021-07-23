# boj 10733 : 제로
> 문제 주소 : https://www.acmicpc.net/problem/10773

### 문제 해결 방향
- 0일때 가장 최근에 넣은 값을 빼야 하므로 stack를 사용한다
- python에서 stack은 그냥 list 를 사용하면 된다.
```python
N = int(input())

money = []
for _ in range(N):
    in_num = int(input())
    if in_num == 0:
        money.pop()
    else:
        money.append(in_num)

print(sum(money))
```