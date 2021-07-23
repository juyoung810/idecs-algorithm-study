### 제로
## 재현이는 잘못된 수를 부를 때마다 0을 외쳐서, 가장 최근에 재민이가 쓴 수를 지우게 시킨다. (0 이전에 온 수를 지워야 한다)
## 이렇게 모든 수를 받아 적은 후 그 수의 합을 알고 싶어 한다.

# 가장 위에 있는 수가 0이면 그 바로 밑에 있는 수를 지운다. 스택을 사용
# 스택은 그냥 리스트를 사용하면 된다.

n = int(input())
stack = []

for i in range(n):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))