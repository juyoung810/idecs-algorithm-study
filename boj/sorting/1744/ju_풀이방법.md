# <span style="color:blue"> boj 1744: 수 묶기 </span>
> 문제 주소: https://www.acmicpc.net/problem/1744
> 
> gold 4

## 문제 해결 방법.
1. 양수를 곱할 경우 값이 더욱 작아지므로 양수, 음수 각각 리스트를 만들어 따로 저장한다.
2. 0의 경우 양수랑 곱해서 더하면 값이 더 작아지지만, 음수를 곱해서 더할 시 값이 더 커지므로 음수 리스트에 저장한다.
3. 양수에서 1이 나오는 경우 , 1를 곱해서 더하는 것 보다 각각 더하면 더 크므로 1이 나온다면, (이미 정렬되어 있으므로) 그 이하는 모두 그냥 더한다.
```python
import sys

N = int(sys.stdin.readline())

# 양수 리스트 생성
p_list = []
# 음수 리스트 생성
n_list = []
for _ in range(N):
    n = int(sys.stdin.readline())
    if n <= 0:
        # 0이 있으면, -1를 그냥 더하는 것 보다 0 곱해서 더하는게 나으므로, 0도 음수 리스트에 넣는다.
        n_list.append(n)
    elif n > 0:
        p_list.append(n)

# 양수는 내림차순 정렬한다.
p_list.sort(reverse=True)
# 음수는 오름차순 정렬한다.
n_list.sort()
result = 0
# 양수 먼저 더한다.
while len(p_list) > 0:
    n1 = p_list.pop(0)
    if len(p_list) != 0:
        n2 = p_list.pop(0)
        # 하나라도 0 이 나오면 n1,n2 그 이하는 모두 그냥 더한다.
        if n1 == 1 or n2 == 1:
            result += n1
            result += n2
            result += sum(p_list)
            break
        # 두 수 모두 1 이 아닐 때, n1*n2
        else:
            result += n1*n2
    # 값이 하나 남았을 경우 그냥 더해준다.
    else:
        
        result += n1

# 음수 더한다.
while len(n_list) > 0:
    n1 = n_list.pop(0)
    if len(n_list) != 0:
        n2 = n_list.pop(0)
        # 음수는 두 수 무조건 곱해서 더한다.
        result += n1*n2
    # 하나 남았을 경우 그냥 더한다.
    else:
        result += n1



sys.stdout.write(str(result))
```