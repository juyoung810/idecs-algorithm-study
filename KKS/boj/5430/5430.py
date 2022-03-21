import sys
from collections import deque
input = sys.stdin.readline

def solve():
    p = list(input().rstrip())
    n = int(input().rstrip())
    target = input().rstrip()
    target = list(target[1:-1].split(','))
    queue = deque(target)
    if n == 0:
        queue = []
    cnt_r = 0
    for item in p:
        if item == 'R':
            cnt_r += 1
        else:
            if len(queue) == 0:
                return print("error")
            if len(queue) >= 1:
                if cnt_r%2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    else:
        if cnt_r%2 == 0:
            print('[' + ','.join(queue) + ']')
        else:
            queue.reverse()
            print('[' + ','.join(queue) + ']')

t = int(input())
for _ in range(t):
    solve()

