# boj 10773 : 제로 by seoyoung
> 문제 주소 https://www.acmicpc.net/problem/10773
> 
> silver 4

## 제로
장부를 관리할 때, 돈을 실수로 잘못 부를 때마다 0을 외쳐서 가장 최근에 쓴 수를 지우고자 한다.
모든 수를 받아 적은 후 그 수의 합을 알고 싶어한다.

## 문제 해결 방향
1. stack 구조를 이용한다. 불러진 수를 스택에 집어넣는데, 수가 0이면 이전의 수를 삭제한다.
2. stack은 파이썬의 리스트와 append, pop 함수를 통해 쉽게 구현 가능
```python
n = int(input())
stack = []

# 숫자를 받아서 스택에 넣는다.
for i in range(n):
    num = int(input())
    # 불러진 수가 0이면 맨 위의 원소를 pop해서 삭제한다.
    if num == 0:
        stack.pop()
    # 아니면 스택에 추가한다.
    else:
        stack.append(num)

print(sum(stack))
```
