N = int(input())

move = []


def hanoi(n, from_pos, to_pos, aux_pos, move):
    if n == 1:
        move.append([from_pos, to_pos])
        return

    # n-1 개의 원반을 보조 기둥으로 이동
    hanoi(n - 1, from_pos, aux_pos, to_pos, move)
    # n-1 개의 원반 이동이 끝난 후 남은 가장 큰 원반을 목적지로 이동
    move.append([from_pos, to_pos])
    # 보조 기둥에 있는 n-1 개를 목적지로 이동
    hanoi(n - 1, aux_pos, to_pos, from_pos, move)


hanoi(N, 1, 3, 2, move)
print(len(move))
for i in range(len(move)):
    f, t = move[i]
    print(f, t)
