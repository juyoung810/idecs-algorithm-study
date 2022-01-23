'''
dictionary -> sort 사용 시 - 264ms
'''
import sys
input = sys.stdin.readline

N = int(input())

file = {}
for _ in range(N):
    fe = input().rstrip().split(".")[1]
    file[fe] = file.get(fe,0) + 1

for key in sorted(file):
    print(key,file[key])

#
# import sys
# from collections import Counter
# input = sys.stdin.readline
#
# N = int(input())
#
# file = []
# for _ in range(N):
#     file.append(input().rstrip().split(".")[1])
# c = Counter(file)
# for key in sorted(c):
#     print(key, c[key])
