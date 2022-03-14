import sys
input = sys.stdin.readline

N, M = map(int, input().split())
s1= set()
s2= set()
for _ in range(N):
    s1.add(input().strip())
for _ in range(M):
    s2.add(input().strip())

s = sorted(list(s1.intersection(s2)))
n = len(s)
print(n)
for i in range(n):
    print(s[i])
    
    
# s = s1.intersection(s2)
# result = [i for i in s]
# n = len(result)
# result.sort()
# print(n)
# for i in range(n):
#     print(result[i])