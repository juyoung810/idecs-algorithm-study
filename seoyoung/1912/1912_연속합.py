'''
n개이 정수로 이루어진 임의의 수열.
연속된 몇 개의 수를 선택해 구할 수 있는 합 중 가장 큰 합을 구하라.

< 아이디어 >
1. 연속된 양수는 그냥 다 더해버린다.
2. 음수를 어떻게 처리하면 좋을까...
3. 더해서 양수면 음수도 더하고, 아니면 안더한다.
'''

n = int(input())
seq = list(map(int, input().split()))
d = seq.copy()

for i in range(1,n):
    if d[i-1]+seq[i] > 0:
        d[i] = d[i-1] + seq[i]
    elif d[i-1]+seq[i] < 0:
        d[i] = max(d[i-1]+seq[i], seq[i])
    if d[i-1] < 0:
        d[i] = seq[i]

print(max(d))