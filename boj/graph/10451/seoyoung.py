'''
순열 사이클
n개의 정수로 이루어진 순열이 주어졌을 때, 순열 사이클의 개수를 구하는 프로그램을 작성하라!
순열의 수에 대해서, 루트 노드를 계속 갱신한다. 갱신한 결과의 부모노드에 대해서, 자기 자신의 값을 갖는 수의 개수를 출력한다.
테스트 케이스의 수가 주어지고, 순열의 크기와 순열이 주어진다. 그 순열에 대한 사이클의 개수를 출력한다.
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(2000)

def dfs(x):
    visited[x] = True
    num = numbers[x-1]
    if not visited[num]:
        dfs(num)


# 입력 데이터 받기
t = int(input())

for case in range(t):
    n = int(input())
    numbers = list(map(int, input().split()))
    visited = [True] + [False] * n
    cnt = 0

    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
            cnt += 1

    print(cnt)