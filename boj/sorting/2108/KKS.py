from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    data.append(int(input()))
data.sort()
#산술평균
print(round(sum(data)/len(data)))
#중앙값
mid = (0 + n)//2
print(data[mid])
#최빈값 -> counter 사용
cnt = Counter(data)
cnt = cnt.most_common()
if len(cnt) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
#범위
print(max(data)-min(data))