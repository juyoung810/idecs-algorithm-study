'''
1. 입력 받은 loop를 크기 큰 순 정렬
2. 현재 index 이전은 무조건 현재 감당 가능한 무게보다 크므로 (index + 1) * 무게가 현재 루프까지
고려 했을때 감당 가능한 최대 무게
'''
import sys

num = int(sys.stdin.readline())

loops = []
for _ in range(num):
    loops.append(int(sys.stdin.readline()))

loops.sort(reverse = True)

ans = 0
for i in range(num):
    if ans < (i+1) * loops[i]:
        ans = (i+1) * loops[i]

print(ans)