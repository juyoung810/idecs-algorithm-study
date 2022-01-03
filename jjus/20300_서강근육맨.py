'''
1. 정렬 후 가장 큰 값을 임시 결과 값으로 지정
2. 홀수 일 경우 -> 가장 마지막 값 제외 가장 작은 값 + 큰 값으로 비교
3. 짝수 일 경우 -> 가장 작은 값 + 큰 값으로 비교

76ms

+) range에 //2 로 정수임을 확실하게 밝히지 않고 /2 로 할 시 TypeError 발생
'''
import sys

input = sys.stdin.readline

N = int(input())
weight = list(map(int,input().rstrip().split()))

result = weight[N-1]
if N % 2 != 0: N -=1

for i in range(N//2):
    if weight[i] + weight[N-1-i] > result:
        result = weight[i] + weight[N-1-i]


print(result)