# 위치에 상관없이 두 수 묶을 수 있다.
# 자기자신을 묶는 것은 불가
# 어떤 수 묶으면, 수열 합 구할 때 묶은 수 서로 곱한 후 더한다.
# 모든 수 단 한번만 묶거나, 아니면 묶지 않아야 한다.
# 수열의 각 수 적절히 묶어서 합이 최대가 될 수 있도록

# 문제 해결 방법
# 1. 양수 정렬 리스트 하나
# 2. 음수 정렬 리스트 하나. -> 내림차순 정렬
# 수를 절댓값 기준 오름차순 정렬해서, 두 수를 두개씩 묶는다.
# 양수에서 둘 중 하나라도 수가 1이면 묶지 않는다. -> 1이 하나라도 나오면 그 이하는 그냥 다 더하는게 값이 더 크다


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