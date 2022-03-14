'''
< 나무 자르기 >

- 절단기에 높이 H를 지정. 한 줄에 연속되어 있는 나무 모두 절단.
- 나무를 필요한 만큼만 집으로 가져가려고 한다.
- 적어도 M미터의 나무를 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하라

< 아이디어 >
- 시작점과 끝점의 중간값에서 자른다.
- 필요한 M보다 크고 작은지의 여부에 따라 다음 중간값에서 자른 값과 비교한다.
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
end = max(trees)
start = 0
result = 0

while (start <= end):
    h = (start+end)//2
    cut = 0
    for tree in trees:
        if tree - h > 0:
            cut += tree - h
    if cut < m:
        end = h - 1
    else:
        result = h
        start = h + 1

print(result)